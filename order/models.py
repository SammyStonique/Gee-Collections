from django.db import models
from product.models import * 
from django.contrib.auth import get_user_model
from product.models import User
import random
import string


UserModel = get_user_model()

def random_string(letter_count=4, digit_count=3):  
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
        str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    
        sam_list = list(str1) # it converts the string to list.  
        random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)  
        return final_string

# Create your models here.
class Order(models.Model):
    id = models.CharField(default=random_string,primary_key=True,max_length=100)
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

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.user.email} ({'%s' % self.id}) Order"


class OrderItem(models.Model) :
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items', on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)


    def __str__(self):
        # return f'{self.product.name} for {self.user.email}' 
        return f"{self.order.email} OrderItem({'%s' % self.id})"


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

    

 