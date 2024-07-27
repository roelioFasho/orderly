# Generated by Django 5.0.7 on 2024-07-27 07:56

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[base.models.validate_non_negative]),
        ),
    ]
