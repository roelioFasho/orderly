from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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


def validate_non_negative(value):
    if value < 0:
        raise ValidationError(
            '%(value)s is not a valid input. The Input must be a non-negative number.',
            params={'value': value},
        )



class Product(models.Model):
    class Currency(models.TextChoices):
        EUR = 'EUR', '€'
        USD = 'USD', '$'
        ALL = 'ALL', 'L'
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6, validators=[validate_non_negative])
    new_price = models.DecimalField(default=0, null=True, decimal_places=2, max_digits=6, validators=[validate_non_negative])
    discount_percentage = models.IntegerField(null=True)
    currency = models.CharField(max_length=5, choices=Currency.choices, default=Currency.ALL)

    date_posted = models.DateField(default=timezone.now)
    # usage = models.CharField(max_length=600)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True, validators=[validate_non_negative])
    image = models.ImageField(blank=True, null=True, upload_to='uploads/product/')
    
    is_discount = models.BooleanField(default= False) 
    out_of_sale = models.BooleanField(default=False)


    @property
    def discount_percentage(self):
        if self.price and self.new_price:
            discount_amount = self.price - self.new_price
            return round((discount_amount / self.price) * 100)
        return None


    def check_for_discount(self):
        if self.new_price != 0:
            self.new_price = True
        else:
            self.new_price = False

        
    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.out_of_sale = True
        else:
            self.out_of_sale = False
        super().save(*args, **kwargs)




    def __str__(self):
        return f"{self.name}"
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'product')






