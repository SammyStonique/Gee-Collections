import os
import re
from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.http import HttpResponse,JsonResponse, FileResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt

##Send Email
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger ##pagination

# PDF REQUIREMENTS
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.views import View

#AFRICASTALKING
import africastalking
username = os.environ.get('AFRICASTALKING_USERNAME')
api_key = os.environ.get('AFRICASTALKING_API_KEY')
africastalking.initialize(username, api_key)  
sms = africastalking.SMS


#Creating PDF using pdfkit
import jinja2   
import pdfkit



# Create your views here.
@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        qset = Order.objects.filter(user=request.user)
        email = qset[0].user
        phone_number = qset[0].phone_number
        customer_name = qset[0].user.first_name
        order_id = qset[0].id
        if(phone_number.startswith("+254")):
            pn = phone_number
        elif(phone_number.startswith('0')):
            pn = re.sub("0","+254",phone_number,1)
        elif (phone_number.startswith('7') or phone_number.startswith('1')):
            pn = "+254"+phone_number
        elif(phone_number.startswith('254')):
            pn = "+"+phone_number
        recipient = [email]
        subject = f'Order Invoice - [{order_id}]'
        content = f'Dear {customer_name}, Thank you for choosing Gee Collections! We appreciate your business and are pleased to provide you with the invoice for your recent order. Below, you will find an attached invoice.'
        # send_mail(subject, content,os.environ.get('EMAIL_HOST_USER'),recipient, fail_silently=False) 
        mail = EmailMessage(subject,content,os.environ.get('EMAIL_HOST_USER'),recipient)
        pdf = orderEmailInvoicePDF(request, order_id)
        mail.attach('Invoice.pdf', pdf, 'application/pdf')
        mail.send(fail_silently = False)

        sms.send(f'Dear {customer_name},your order {order_id} has succesfully been placed. Thank you for doing business with us.',[f'{pn}'],callback=checkout)
        return Response(serializer.data)

class OrdersList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = MyOrderSerializer

class MpesaDetails(generics.ListAPIView):
    queryset = MpesaPayment.objects.all()
    serializer_class = MpesaPaymentSerializer

def getAccessToken(request):
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

@api_view(['POST'])
def lipa_na_mpesa_online(request):
    payment_number = request.data.get('payment_number')
    first_name = request.data.get('first_name')
    orderTotal = request.data.get('orderTotal')
    print('The number used to pay is ',payment_number)
    print('The payee name is ',first_name)
    print('The amount to pay is ',orderTotal)

    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": payment_number,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": payment_number,  # replace with your phone number to get stk push
        "CallBackURL": "https://d0a8-41-81-221-21.ngrok-free.app/api/v1/c2b/callback",
        "AccountReference": first_name,
        "TransactionDesc": "Making payment for purchased goods"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://d0a8-41-81-221-21.ngrok-free.app/api/v1/c2b/confirmation",
               "ValidationURL": "https://d0a8-41-81-221-21.ngrok-free.app/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):  
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    print('this is the body:',mpesa_body)
    if(mpesa_payment['Body']['stkCallback']['ResultCode'] == 0):
        amount = mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][0].get('Value')
        phone_number=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4].get('Value')
        payment= MpesaPayment(
            transaction_time=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][3].get('Value'),
            amount=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][0].get('Value'),
            phone_number=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4].get('Value'),
            transaction_id=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][1].get('Value'),
        )
        payment.save()
        # sms.send(f'Confirmed,we have received your payment of {amount}. Thank you for doing business with us.',[f'+{phone_number}'],callback=call_back)
    else:
        result = mpesa_payment['Body']['stkCallback']['ResultDesc']
        print(result)

    return JsonResponse(mpesa_body,safe=False)

@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    print('this is the confirmation body:',mpesa_body)
    payment = MpesaPayment(
        transaction_type=mpesa_payment['TransactionType'],
        transaction_id=mpesa_payment['TransID'],
        transaction_time=mpesa_payment['TransTime'],
        amount=mpesa_payment['TransAmount'],
        phone_number=mpesa_payment['MSISDN'],
        invoice_number=mpesa_payment['InvoiceNumber'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        shortcode=mpesa_payment['BusinessShortCode'],
        third_party_transaction_id=mpesa_payment['ThirdPartyTransID'],
        first_name=mpesa_payment['FirstName'],
        # middle_name=mpesa_payment['MiddleName'],
        # last_name=mpesa_payment['LastName'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


def orderEmailInvoicePDF(request,order_id):
    myOrder = get_object_or_404(Order, pk=order_id)
    orderItems = OrderItem.objects.filter(order=myOrder)

    for orderItem in orderItems:
        product_name = orderItem.product.name
        product_price = orderItem.product.price
        quantity = orderItem.quantity
        price = orderItem.price

    invoice_no = myOrder.id
    first_name = myOrder.first_name
    last_name = myOrder.last_name
    address = myOrder.address
    city = myOrder.city
    county = myOrder.county
    subtotal = quantity * price
    order_total = myOrder.order_total
    invoice_date = myOrder.created_at.strftime("%d %b, %Y")
    month = myOrder.created_at.strftime("%B")

    context={"order_id":invoice_no, "order_first_name":first_name, "order_last_name":last_name,
              "order_address":address, "order_city":city, "order_county":county, 
              "order_total ":order_total, "product_name":product_name, "product_price":product_price,
              "quantity":quantity, "price":price , "month":month , "invoice_date":invoice_date , "subtotal":subtotal}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/gee_collections/order/templates/order/')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('order_invoice.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Invoice.pdf', configuration=config, options=options, css="/home/sammyb/gee_collections/order/static/order/invoice-pdf.css")

    path = 'Invoice.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    # response = HttpResponse(contents, content_type='application/pdf')

    # response['Content-Disposition'] = 'attachment; filename=Invoice.pdf'
    pdf.close()
    os.remove("Invoice.pdf")  # remove the locally created pdf file.
    return contents  

def orderInvoicePDF(request,order_id):
    myOrder = get_object_or_404(Order, pk=order_id)
    orderItems = OrderItem.objects.filter(order=myOrder)

    for orderItem in orderItems:
        product_name = orderItem.product.name
        product_price = orderItem.product.price
        quantity = orderItem.quantity
        price = orderItem.price

    invoice_no = myOrder.id
    first_name = myOrder.first_name
    last_name = myOrder.last_name
    address = myOrder.address
    city = myOrder.city
    county = myOrder.county
    subtotal = quantity * price
    order_total = myOrder.order_total
    invoice_date = myOrder.created_at.strftime("%d %b, %Y")
    month = myOrder.created_at.strftime("%B")

    context={"order_id":invoice_no, "order_first_name":first_name, "order_last_name":last_name,
              "order_address":address, "order_city":city, "order_county":county, 
              "order_total ":order_total, "product_name":product_name, "product_price":product_price,
              "quantity":quantity, "price":price , "month":month , "invoice_date":invoice_date , "subtotal":subtotal}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/gee_collections/order/templates/order/')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('order_invoice.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Invoice.pdf', configuration=config, options=options, css="/home/sammyb/gee_collections/order/static/order/invoice-pdf.css")

    path = 'Invoice.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Invoice.pdf'
    pdf.close()
    os.remove("Invoice.pdf")  # remove the locally created pdf file.
    return response
