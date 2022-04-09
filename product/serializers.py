from rest_framework import serializers
import jsonpickle
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','phone_number','gender','birthdate','city','county','address']


class ProductSerializer(serializers.ModelSerializer):
    categories = Category.objects.all()
    category = jsonpickle.encode(serializers.ChoiceField(choices=categories))   
    class Meta:
        model = Product
        fields = ['id','name','slug','description','category','price','image','thumbnail',
            'date_added','get_absolute_url']
        

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = Category
        fields = ['id','name','slug','get_absolute_url','products']
