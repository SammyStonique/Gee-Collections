# Generated by Django 5.0 on 2024-01-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0032_added_created_at_field_to_receipt_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='created_at',
            field=models.DateField(),
        ),
    ]