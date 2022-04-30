# Generated by Django 4.0.3 on 2022-04-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_mpesapayment_invoice_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='organization_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='mpesapayment',
            name='third_party_transaction_id',
            field=models.CharField(max_length=250),
        ),
    ]