from rest_framework import serializers
from .models import *
from product.serializers import *

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['ordered','quantity','product','user']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['ordered','items','created_at','user','first_name','last_name','email','phone_number','address','city']