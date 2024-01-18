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
from django.core.mail import EmailMessage, EmailMultiAlternatives
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
        # orderItems = OrderItem.objects.get(order=qset)

        email = qset[0].user
        phone_number = qset[0].phone_number
        customer_name = qset[0].user.first_name
        order_id = qset[0].id
        billing_address = qset[0].address
        city = qset[0].city
        shipping_cost = qset[0].delivery_fee
        transaction_id = qset[0].payment_reference
        payment_status = qset[0].paid
        subtotal = qset[0].order_total
        total_due = qset[0].order_total + qset[0].delivery_fee
        # for orderItem in orderItems:
        #     product_name = orderItem.product.name
        #     quantity = orderItem.quantity
        #     price = orderItem.price
        #     price_total = quantity * price

        vat = 0
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
        template_loader = jinja2.FileSystemLoader('/home/sammyb/gee_collections/order/templates/order/')
        template_env = jinja2.Environment(loader=template_loader)
        # output_text = {"customer_name": customer_name, "order_id": order_id, "billing_address": billing_address, "city": city,
        #                "shipping_cost": shipping_cost, "transaction_id": transaction_id, "payment_status": payment_status,
        #                 "total_due": total_due, "subtotal": subtotal, "vat": vat,  "product_name": product_name,
        #                 "quantity": quantity, "price": price, "price_total": price_total}
        output_text = {"customer_name": customer_name, "order_id": order_id, "billing_address": billing_address, "city": city,
                       "shipping_cost": shipping_cost, "transaction_id": transaction_id, "payment_status": payment_status,
                        "total_due": total_due, "subtotal": subtotal, "vat": vat}

        template  = template_env.get_template('invoice_email.html')
        content = template.render(output_text)
        mail = EmailMultiAlternatives(subject,content,os.environ.get('EMAIL_HOST_USER'),recipient)
        mail.attach_alternative(content, "text/html")
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

@api_view(['POST'])
def couponGen(request):
    coupon_amount = request.data.get('coupon_amount')
    print("The coupon amount is ", coupon_amount)
    serializer = CouponSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        qset = Coupon.objects.filter(user=request.user)
        customer_name = qset[0].user.first_name
        phone_number = qset[0].coupon_order.phone_number
        coupon_code = qset[0].coupon_code

        if(phone_number.startswith("+254")):
            pn = phone_number
        elif(phone_number.startswith('0')):
            pn = re.sub("0","+254",phone_number,1)
        elif (phone_number.startswith('7') or phone_number.startswith('1')):
            pn = "+254"+phone_number
        elif(phone_number.startswith('254')):
            pn = "+"+phone_number
        
        sms.send(f'Dear {customer_name},as a token of our appreciation, we are thrilled to present you with an exclusive coupon code to use on your next purchase. The code is {coupon_code} and is worth {coupon_amount}',[f'{pn}'],callback=couponGen)
        return Response(serializer.data)
    else:
        return Response('Coupon not generated')

class CouponsList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

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
        "CallBackURL": "https://faec-197-156-140-162.ngrok-free.app/api/v1/c2b/callback",
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
               "ConfirmationURL": "https://faec-197-156-140-162.ngrok-free.app/api/v1/c2b/confirmation",
               "ValidationURL": "https://faec-197-156-140-162.ngrok-free.app/api/v1/c2b/validation"}
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

    invoice_no = myOrder.invoice_no
    first_name = myOrder.first_name
    last_name = myOrder.last_name
    address = myOrder.address
    city = myOrder.city
    county = myOrder.county
    order_total = myOrder.order_total
    invoice_date = myOrder.created_at.strftime("%d %b, %Y")
    month = myOrder.created_at.strftime("%B")

    context={"orderItems": orderItems, "invoice_no":invoice_no, "order_first_name":first_name, "order_last_name":last_name,
              "order_address":address, "order_city":city, "order_county":county, 
              "order_total ":order_total, "month":month , "invoice_date":invoice_date }

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


    invoice_no = myOrder.invoice_no
    first_name = myOrder.first_name
    last_name = myOrder.last_name
    address = myOrder.address
    city = myOrder.city
    county = myOrder.county
    order_total = myOrder.order_total
    invoice_date = myOrder.created_at.strftime("%d %b, %Y")
    month = myOrder.created_at.strftime("%B")

    context={"orderItems": orderItems,"invoice_no":invoice_no, "order_first_name":first_name, "order_last_name":last_name,
              "order_address":address, "order_city":city, "order_county":county, 
              "order_total ":order_total, "month":month , "invoice_date":invoice_date}

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



def orderReceiptPDF(request,order_id):
    myOrder = get_object_or_404(Order, pk=order_id)
    orderItems = OrderItem.objects.filter(order=myOrder)
    myReceipt = get_object_or_404(Receipt, receipt_order=myOrder)

    receipt_no = myReceipt.receipt_no
    received_by = myReceipt.received_by
    balance = myReceipt.balance
    reference_no = myReceipt.reference_no
    customer_name = myOrder.last_name + myOrder.first_name
    phone_number = myOrder.user.phone_number
    email = myOrder.email
    address = myOrder.address
    city = myOrder.city
    county = myOrder.county
    order_total = myOrder.order_total
    receipt_date = myReceipt.created_at.strftime("%d %b, %Y")
    month = myOrder.created_at.strftime("%B")

    context={"orderItems": orderItems,"receipt_no":receipt_no, "customer_name":customer_name, "phone_number":phone_number,
              "payment_method":address, "reference_no":reference_no, "amount":county, 
              "balance ":balance, "month":month , "date":receipt_date , "address":address,
              "county":county, "email":email, "received_by": received_by,"order_total":order_total}

    template_loader = jinja2.FileSystemLoader('/home/sammyb/gee_collections/order/templates/order/')
    template_env = jinja2.Environment(loader=template_loader)

    template  = template_env.get_template('order_receipt.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    options={"enable-local-file-access": None,
             }

    pdfkit.from_string(output_text, 'Receipt.pdf', configuration=config, options=options, css="/home/sammyb/gee_collections/order/static/order/invoice-pdf.css")

    path = 'Receipt.pdf'
    with open(path, 'rb') as pdf:
        contents = pdf.read()

    response = HttpResponse(contents, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=Receipt.pdf'
    pdf.close()
    os.remove("Receipt.pdf")  # remove the locally created pdf file.
    return response

