from django.contrib import admin
from .models import Category, SubCategory, Product
from cart.models import CartItem

# admin.site.register(Costumer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(CartItem)

