from rest_framework import serializers
from .models import *
from product.serializers import *

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['product','quantity','price']

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','user','first_name','last_name','email','phone_number','county','city','address','items','created_at','order_total','paid']


class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = OrderItem
        fields = ['product','quantity','price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Order
        fields = ['id','user','first_name','last_name','email','phone_number','county','city','address','items','created_at','order_total','paid']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order
