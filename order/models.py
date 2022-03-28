from django.db import models
from product.models import * 
from django.contrib.auth.models import User

# Create your models here.
class OrderItem(models.Model) :
    user = models.ForeignKey('auth.User',related_name='orderitems', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"


class Order(models.Model):
    user = models.ForeignKey('auth.User',related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ('-ordered_date',)
    
    def __str__(self):
        return f'{self.user.username} Order'

    

 