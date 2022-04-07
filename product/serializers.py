from rest_framework import serializers
import jsonpickle
from .models import *

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

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ['user','first_name','last_name','birthdate','gender','city','county','address']

    def create(self, validated_data):
        """
        Create and return a new `Profile` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Profile` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.city = validated_data.get('city', instance.city)
        instance.county = validated_data.get('county', instance.county)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance