from django_filters import rest_framework as filters
from .models import *
from django_filters import CharFilter

class ProductsFilter(filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    description = CharFilter(field_name='description',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','description']