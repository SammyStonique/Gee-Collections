# Generated by Django 4.0.3 on 2022-04-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_rename_type_mpesapayment_transaction_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpesapayment',
            old_name='description',
            new_name='invoice_number',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='shortcode',
            field=models.CharField(default='invoice', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='third_party_transaction_id',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='transaction_id',
            field=models.CharField(default='id', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='transaction_time',
            field=models.TextField(default='time'),
            preserve_default=False,
        ),
    ]