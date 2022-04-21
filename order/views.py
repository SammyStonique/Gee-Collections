import os
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from django.http import HttpResponse,JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class CheckOut(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def getAccessToken(request):
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254795968217,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254795968217,  # replace with your phone number to get stk push
        "CallBackURL": "https://f055-197-248-34-79.ngrok.io/api/v1/c2b/callback",
        "AccountReference": "SammyB",
        "TransactionDesc": "Testing stk push"
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
               "ConfirmationURL": "https://f055-197-248-34-79.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://f055-197-248-34-79.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    print('this is the body:',mpesa_body)
    amount = mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][0].get('Value')
    print('The amount is:',amount)
    payment= MpesaPayment(
        transaction_time=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][3].get('Value'),
        amount=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][0].get('Value'),
        phone_number=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4].get('Value'),
        transaction_id=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][1].get('Value'),
    )
    payment.save()
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
        middle_name=mpesa_payment['MiddleName'],
        last_name=mpesa_payment['LastName'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))