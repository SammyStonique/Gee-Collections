from django.db import models
from product.models import * 
from django.contrib.auth import get_user_model
from product.models import User


UserModel = get_user_model()
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(UserModel,related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    order_total = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.user.email} ({'%s' % self.id}) Order"


class OrderItem(models.Model) :
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        # return f'{self.product.name} for {self.user.email}' 
        return f"{self.order.email} OrderItem({'%s' % self.id})"




    

 