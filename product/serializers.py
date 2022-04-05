from rest_framework import serializers
import jsonpickle
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    categories = Category.objects.all()
    # objects.all()
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

# class ProfileSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model = Profile
#         fields = ['username','first_name','last_name','birthdate','gender','phone_number','city','county','address']