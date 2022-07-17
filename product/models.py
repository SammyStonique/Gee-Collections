from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email,phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,phone_number, password, **other_fields)


    def create_user(self, email,phone_number,password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    CITY = (('','Select your city'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Kisumu','Kisumu'),('Nakuru','Nakuru'))
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other')) 
    COUNTY = (('','Select County'),('Kisumu','Kisumu'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Siaya','Siaya'))
    
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=250,blank=True)
    last_name = models.CharField(max_length=250,blank=True)
    birthdate = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=250,choices=GENDER,default='',blank=True)
    phone_number = models.CharField(max_length=250)
    city = models.CharField(max_length=250,choices=CITY,default='',blank=True)
    county = models.CharField(max_length=250,choices=COUNTY,default='',blank=True)
    address = models.CharField(max_length=250,blank=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= False)
    start_date = models.DateTimeField(auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name','birthdate','gender','city','county','address']

    def __str__(self):
        return f'{self.email}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Product(models.Model):

    category= models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8080' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8080' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8080' + self.thumbnail.url
            else:
                return ''
    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


