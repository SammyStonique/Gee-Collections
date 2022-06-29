from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.urls import reverse

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)
order_name.short_description = 'Name'

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))
order_name.short_description = 'PDF'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'paid', 'created_at', order_pdf]
    list_filter = ['created_at', 'paid']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]
    # actions = [admin_order_shipped]

# Register your models here.
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(MpesaPayment)
admin.site.register(PaymentDetail)