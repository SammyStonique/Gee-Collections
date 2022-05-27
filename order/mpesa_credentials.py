import os
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    print('THe consumer key is:', MpesaC2bCredential.consumer_key)
    print('THe consumer secret is:', MpesaC2bCredential.consumer_secret)
    print('The value of r is:', r)
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    # print('THe consumer key is:', MpesaC2bCredential.consumer_key)
    # print('THe consumer secret is:', MpesaC2bCredential.consumer_secret)
    # encoded_key = os.environ.get('CONSUMER_KEY')+":"+os.environ.get('CONSUMER_SECRET')
    # encoded_key_bytes = encoded_key.encode("ascii")
    # base64_bytes = base64.b64encode(encoded_key_bytes)
    # base64_string = base64_bytes.decode("ascii")
    # response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': f'Bearer {base64_string}' })
    # print(response.text.encode('utf8'))

class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')