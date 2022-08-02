import os
from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from djoser.views import UserViewSet
from rest_framework.decorators import api_view
import requests
import smtplib
from django.core.mail import send_mail

# Create your views here.

class LatestProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'

class ProductCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def newsletter_email(request):
    email = request.data.get('email')
    serializer = NewsletterSubscriptionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        recipient = [email]
        subject = f'Newsletter Subscription'
        content = f'Dear Client, You have succesfully subscribed to our newsletter. We will keep you posted at all times. Thank you.'
        send_mail(subject, content,os.environ.get('EMAIL_HOST_USER'),recipient, fail_silently=False) 
        return Response(serializer.data)

class NewsletterEmails(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer