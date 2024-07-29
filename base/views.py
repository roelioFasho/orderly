from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse

from .models import Product, Wishlist
from django.contrib import messages



def index(request):
    product = Product.objects.filter()
    return render(request, "base/home.html", {'products':product} )



def product_view(request, name):
    product = Product.objects.get(name=name)
    return render(request, "base/product.html", {'product':product})



def product_view2(request):
    product = Product.objects.filter()
    return render(request, "base/login.html", {'products':product})





@require_POST
@login_required
def add_to_wishlist(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        return JsonResponse({'status': 'success', 'message': 'Product added to wishlist.'})
    else:
        return JsonResponse({'status': 'info', 'message': 'Product is already in your wishlist.'})

@login_required
def wishlist_display(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products = [item.product for item in wishlist_items]
    for product in products:
        print(product.name)

    # return render(request, 'base/wishlist.html', {'products': products})

# @login_required
# def wishlist_view(request, id):
#     product = get_object_or_404(Product, id=id)
#     # check if user has added the product to the wishlist
#     if product.users_wishlist.filter(id=request.user.id).exists():


# @login_required
# def wishlist_view(request, id):
#     product = get_object_or_404(Product, id=id)
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
#     if created:
#         messages.success(request, f"{product.name} has been added to your wishlist.")
#         #return render('base/wishlist.html', pk=product.id)
#         return render(request, 'base/wishlist.html', )
#     else:
#         messages.info(request, f"{product.name} is already in your wishlist.")




# @login_required
# def wishlist_view(request, id):
#     wishlist = Wishlist.objects.all()
#     context ={
#         'w': wishlist
#     }
#     return render(request, "base/wishlist.html", context)

# def add_to_wishlist(request):
#     product_id = request.GET['ID']
#     product = Product.objects.get(id=product_id)
#     context = {}

#     wishlistcount = Wishlist.objects.filter(product=product, user=request.user).count()
#     print(wishlistcount)
#     if wishlistcount > 0:
#         context = {
#             'bool': True
#         }

#     else:
#         new_wishlist = Wishlist.objects.create(
#             product = product,
#             user = request.user
#         )
#     context = {
#             'bool': True
#         }

#     return (request, context)



"""
from base.models import Wishlist
from django.contrib.auth.models import User

user = User.objects.get(username='admin')
wishlist_items = Wishlist.objects.filter(user=user)
ab =[item for item in wishlist_items]
    print(item.product.name)
   

"""
    

def privacy_policy_view(request):
    return render(request, "base/privacy_policy.html" )


def terms_service_view(request):
    return render(request, "base/terms_of_service.html" )
