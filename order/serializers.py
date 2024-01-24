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
    
class CouponSerializer(serializers.ModelSerializer):
    # coupon_order = serializers.PrimaryKeyRelatedField(queryset = Order.objects.all())
    coupon_order = serializers.ReadOnlyField(source='coupon_order.id')
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Coupon
        fields=['coupon_code','coupon_amount','user','coupon_order','created_at']

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
    

