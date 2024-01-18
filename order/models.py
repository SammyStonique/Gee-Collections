from django.db import models
from product.models import * 
from django.contrib.auth import get_user_model
from product.models import User
import random
import string


UserModel = get_user_model()

#Function to generate random string that serves as order ID
def random_string(letter_count=4, digit_count=3):  
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
        str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    
        sam_list = list(str1) # it converts the string to list.  
        random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)  
        return final_string

#Function to generate random string that serves as coupon code
def coupon_generator(letter_count=4, digit_count=2):  
        str1 = ''.join((random.choice(string.ascii_uppercase) for x in range(letter_count)))  
        str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    
        sam_list = list(str1) # it converts the string to list.  
        random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)  
        return final_string

# #Function to generate incrementing invoice numbers
def invoice_number_gen():
        last_invoice = Order.objects.all().order_by('invoice_no').last()
        if not last_invoice:
            return "INV0001"
        invoice_no = last_invoice.invoice_no
        invoice_int = int(invoice_no.split('INV')[-1])
        new_invoice_int = invoice_int + 1
        new_invoice_no = 'INV'+ str(new_invoice_int).zfill(4)
        
        return new_invoice_no


#Function to generate incrementing receipt numbers
def receipt_number_gen():
        last_receipt = Receipt.objects.all().order_by('receipt_no').last()
        if not last_receipt:
            return "RC0001"
        receipt_no = last_receipt.receipt_no
        receipt_int = int(receipt_no.split('RC')[-1])
        new_receipt_int = receipt_int + 1
        new_receipt_no = 'RC'+ str(new_receipt_int).zfill(4)

        return new_receipt_no


# Create your models here.
class Order(models.Model):
    id = models.CharField(default=random_string,primary_key=True,max_length=100)
    invoice_no = models.CharField(default=invoice_number_gen, max_length=250)
    user = models.ForeignKey(UserModel,related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.user.email} ({'%s' % self.id}) Order"


class OrderItem(models.Model) :

    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items', on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)

    def getTotal(self):
         return self.quantity * self.price

    def __str__(self):
        return f"{self.order.email} OrderItem({'%s' % self.order.id})"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'

class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'
        
class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=250)
    transaction_time = models.CharField(max_length=250)
    transaction_type = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    invoice_number= models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=250)
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    shortcode = models.CharField(max_length=250)
    third_party_transaction_id = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.transaction_id

class Coupon(models.Model):
    coupon_code = models.CharField(default=coupon_generator,primary_key=True,max_length=100)
    coupon_amount = models.DecimalField(max_digits=8, decimal_places=2)
    coupon_order = models.ForeignKey(Order,related_name='coupon_order',on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel,related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.coupon_order.email}({'%s' % self.coupon_order.id}) - {'%s' % self.coupon_code}"
    
class Receipt(models.Model):
    PAYMETHOD = (('','Payment Method'),('Cash','Cash'),('Mpesa','Mpesa'),('Cheque','Cheque'),('EFT','EFT'))

    receipt_no = models.CharField(default=receipt_number_gen,primary_key=True, max_length=100)
    receipt_order = models.ForeignKey(Order, related_name = "receipt_order", on_delete=models.CASCADE)
    receipt_user = models.ForeignKey(UserModel,related_name='receipt_user', on_delete=models.CASCADE)
    received_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=250, choices=PAYMETHOD ,default='', blank=True)
    received_by = models.CharField(max_length=250, blank=True)
    reference_no = models.CharField(max_length=250, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.receipt_no} - Order ({self.receipt_order.id})"



