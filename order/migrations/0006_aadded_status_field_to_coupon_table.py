# Generated by Django 5.0.1 on 2024-02-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_added_coupon_applied_field_to_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='activation_status',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='validity',
        ),
        migrations.AddField(
            model_name='coupon',
            name='status',
            field=models.CharField(choices=[('', 'Coupon Status'), ('Inactive', 'Inactive'), ('Activated', 'Activated'), ('Used', 'Used'), ('Expired', 'Expired')], default='Inactive', max_length=250),
        ),
    ]