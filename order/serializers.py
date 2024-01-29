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
        fields = ['id','user','first_name','last_name','email','phone_number','county','city','address','items','created_at','order_total','paid','payment_reference']


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
        fields = ['id','user','first_name','last_name','email','phone_number','county','city','address','items','created_at','order_total','paid','payment_reference','delivery_fee','invoice_no']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order
    
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        itemArr = []
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.county = validated_data.get('county', instance.county)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.order_total = validated_data.get('order_total', instance.order_total)
        instance.paid = validated_data.get('paid', instance.paid)
        instance.payment_reference = validated_data.get('payment_reference', instance.payment_reference)
        instance.delivery_fee = validated_data.get('delivery_fee', instance.delivery_fee)

        instance.save()
        return instance
    
class CouponSerializer(serializers.ModelSerializer):
    coupon_user = serializers.ReadOnlyField(source='coupon_user.email')
    class Meta:
        model = Coupon
        fields=['coupon_code','coupon_amount','coupon_user','coupon_order','created_at','activation_status']

    def create(self, validated_data):
        coupon = Coupon.objects.create(**validated_data)
            
        return coupon

class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields=['transaction_id','phone_number','amount','transaction_time']

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields=['receipt_no','receipt_order','receipt_user','received_amount','payment_method','received_by','reference_no','balance','created_at']

    def create(self, validated_data):
        receipt = Receipt.objects.create(**validated_data)
            
        return receipt
    
    

