from django.db import models
from base.models import Product
from django.contrib.auth.models import User

# Create your models here.


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'product')