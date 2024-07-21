from base.models import Product
from django.db import models



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Cart {self.id}'
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.FloatField
    def __str__(self):
        return f'{self.total}'
