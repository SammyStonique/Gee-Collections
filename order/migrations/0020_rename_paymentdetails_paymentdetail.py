# Generated by Django 4.0.3 on 2022-06-29 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_paymentdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentDetails',
            new_name='PaymentDetail',
        ),
    ]