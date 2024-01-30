import os
from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from django_filters import rest_framework as filters
from django_filters import CharFilter
from .serializers import *
from rest_framework.decorators import api_view
from django.core.mail import send_mail

# Create your views here.

class ProductsFilter(filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    description = CharFilter(field_name='description',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','description']

class LatestProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductsFilter


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
    else:
        return Response('No email provided')

class NewsletterEmails(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer