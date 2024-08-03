from django.shortcuts import get_object_or_404, redirect, render

# Creafrom django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
from base.models import Product
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



 
# def view_cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart:view_cart')
 
# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id)
#     cart_item.delete()
#     return redirect('cart:view_cart')
 
 
# def home(request):
#     return redirect('home')


# @login_required(login_url="/members/login/")
def cart_view(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    return render(request, 'cart/cart.html',{'cart_products': cart_products, 'quantities': quantities})

@login_required(login_url="/members/login/")
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        

        cart.add(product=product, quantity=product_qty)

        #get cart quantity
        cart_quantity = len(cart)

        # respone = JsonResponse({"Product name: ": product.name})
        respone = JsonResponse({"qty": cart_quantity})
        return respone

    return render(request, 'cart/cart.html')

# @login_required(login_url="/members/login/")
def cart_delete(request):
    return render(request, 'cart/cart.html')


# @login_required(login_url="/members/login/")
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)   
    response = JsonResponse({'qty': product_qty})
    return response
    