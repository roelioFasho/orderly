# Generated by Django 5.0.7 on 2024-07-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_product_discount_percentage_product_new_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discont_price',
        ),
    ]
