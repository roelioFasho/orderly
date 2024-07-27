from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.utils import timezone


class Costumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50)
    email =models.EmailField(max_length=120)
    password =models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


#categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'



# SubCategory Model
class SubCategory(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, related_name="subcategories", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subcategories'



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    date_posted = models.DateField(default=timezone.now)
    usage = models.CharField(max_length=600)
    quantity = models.IntegerField
    image = models.ImageField(blank=True, null=True, upload_to='uploads/product/')
    # reviews = 
    # date_posted = 

    # out_of_sale
    # is_sale




    def __str__(self):
        return self.name