# Generated by Django 4.0.3 on 2022-04-07 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_category_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
