from rest_framework import serializers
from .models import *
from product.serializers import *
from users.serializers import *

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
        fields = ['id','user','first_name','last_name','email','phone_number','county','city','address','items','created_at','order_total','paid','payment_reference','delivery_fee','invoice_no','receipt_no','coupon_applied']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order
    
    def update(self, instance, validated_data):
        instance.paid = validated_data.get('paid', instance.paid)
        instance.payment_reference = validated_data.get('payment_reference', instance.payment_reference)
        instance.receipt_no = validated_data.get('receipt_no', instance.receipt_no)

        instance.save()
        return instance
    
class CouponSerializer(serializers.ModelSerializer):
    coupon_user = serializers.ReadOnlyField(source='coupon_user.email')
    class Meta:
        model = Coupon
        fields=['coupon_code','coupon_amount','coupon_user','coupon_order','created_at','status']

    def create(self, validated_data):
        coupon = Coupon.objects.create(**validated_data)
            
        return coupon
    def update(self, instance, validated_data):

        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance


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
    
    
    
    

