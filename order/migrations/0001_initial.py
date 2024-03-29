# Generated by Django 5.0.1 on 2024-01-30 05:23

import order.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_code', models.CharField(default=order.models.coupon_generator, max_length=100, primary_key=True, serialize=False)),
                ('coupon_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activation_status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='MpesaCallBacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip_address', models.TextField()),
                ('caller', models.TextField()),
                ('conversation_id', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Mpesa Call Back',
                'verbose_name_plural': 'Mpesa Call Backs',
            },
        ),
        migrations.CreateModel(
            name='MpesaCalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip_address', models.TextField()),
                ('caller', models.TextField()),
                ('conversation_id', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Mpesa Call',
                'verbose_name_plural': 'Mpesa Calls',
            },
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=250)),
                ('transaction_time', models.CharField(max_length=250)),
                ('transaction_type', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('invoice_number', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=250)),
                ('organization_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shortcode', models.CharField(max_length=250)),
                ('third_party_transaction_id', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Mpesa Payment',
                'verbose_name_plural': 'Mpesa Payments',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=order.models.random_string, max_length=100, primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(default=order.models.invoice_number_gen, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('receipt_no', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_no', models.CharField(default=order.models.receipt_number_gen, max_length=100, primary_key=True, serialize=False)),
                ('received_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_method', models.CharField(choices=[('', 'Payment Method'), ('Cash', 'Cash'), ('Mpesa', 'Mpesa'), ('Cheque', 'Cheque'), ('EFT', 'EFT')], default='Cash', max_length=250)),
                ('received_by', models.CharField(blank=True, max_length=250)),
                ('reference_no', models.CharField(max_length=250)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateField()),
            ],
        ),
    ]
