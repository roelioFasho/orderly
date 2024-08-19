from django.shortcuts import get_object_or_404, redirect, render

# from .models import CartItem
from base.models import Product
from .wish import Wishlist
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required




#view cart
def cart_view(request):
    #get cart
    cart = Wishlist(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    total = cart.total()

    tuple_output = Product.objects.values_list('currency', flat=True).first()
    product_currency = ''.join(tuple_output)

    return render(request, 'wishlist/wishlist.html',{'cart_products': cart_products, 'quantities': quantities, 'total':total, 'product_curr': product_currency})


#add product to cart
@login_required(login_url="/members/login/")
def cart_add(request):
    cart = Wishlist(request)
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

    return render(request, 'wishlist/wishlist.html')



# remove itm from cart 
def cart_delete(request):
    cart = Wishlist(request)
    print(f"cart delete {cart}") 
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        # call delete func in cart
        cart.delete(product=product_id)
        response = JsonResponse({'id1': product_id})
        return response



# update the cart
def cart_update(request):
    cart = Wishlist(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)  
    response = JsonResponse({'qty': product_qty})
    return response
    