from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.

class CheckOut(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
