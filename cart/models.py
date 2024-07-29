from base.models import Product
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


# class Cart(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'Cart {self.id}'
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.product}'
