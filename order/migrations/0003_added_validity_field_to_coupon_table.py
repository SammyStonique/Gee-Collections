# Generated by Django 5.0.1 on 2024-01-31 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='validity',
            field=models.BooleanField(default=False),
        ),
    ]
