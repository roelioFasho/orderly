from django.shortcuts import get_object_or_404, redirect, render

# Creafrom django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from base.models import Product




from django.shortcuts import render, redirect
from .models import Product, CartItem
 
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'myapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
 
 
def home(request):
    return redirect('home')

def cart_view(request):
    return render(request, 'cart/cart.html')
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_id = request.session.get('cart_id')
#     if not cart_id:
#         cart = Cart.objects.create()
#         request.session['cart_id'] = cart.id
#     else:
#         cart = Cart.objects.get(id=cart_id)

#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not created:
#         cart_item.total += Product.price
#         cart_item.save()

#     return redirect('cart:cart_detail')

# def cart_detail(request):
#     cart_id = request.session.get('cart_id')
#     if not cart_id:
#         return render(request, 'cart/cart.html', {'cart': None})
#     cart = Cart.objects.get(id=cart_id)
#     return render(request, 'cart/cart.html', {'cart': cart})
