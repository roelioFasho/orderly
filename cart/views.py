from django.shortcuts import get_object_or_404, redirect, render

# Creafrom django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
from base.models import Product
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



 
#view cart
def cart_view(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    return render(request, 'cart/cart.html',{'cart_products': cart_products, 'quantities': quantities})


#add product to cart
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



# remove itm from cart 
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        # call delete func in cart
        cart.delete(product=product_id)
        response = JsonResponse({'id1': product_id})
        return response



# update the cart
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)   
    response = JsonResponse({'qty': product_qty})
    return response
    