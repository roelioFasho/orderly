# Generated by Django 5.0.7 on 2024-07-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
