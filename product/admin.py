from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'phone_number','first_name',)
    list_filter = ('email', 'phone_number','first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email','phone_number', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('phone_number','address','birthdate','gender','city','county')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2','phone_number','address','birthdate','gender','city','county', 'is_active', 'is_staff')}
         ),
    )
admin.site.register(User,UserAdminConfig)