# Generated by Django 5.0.1 on 2024-01-30 05:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='coupon_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coupon',
            name='coupon_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_orders', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_order', to='order.order'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_user', to=settings.AUTH_USER_MODEL),
        ),
    ]