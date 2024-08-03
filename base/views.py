from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse

from .models import Category, Product, Wishlist
from django.contrib import messages



def index(request):
    product = Product.objects.filter()
    return render(request, "base/home.html", {'products':product})

def privacy_policy_view(request):
    return render(request, "base/privacy_policy.html" )


def terms_service_view(request):
    return render(request, "base/terms_of_service.html" )



def product_view(request, name):
    product = Product.objects.get(name=name)
    return render(request, "base/product.html", {'product':product})




@login_required(login_url="/members/login/")
def wishlist_display(request):
    return(request, 'base/wishlist.html')



# def game_view(request):
#     product = Product.objects.filter()
#     # category_name = 'VideoGame'
#     # products = Product.objects.filter(name=category_name)
#     # if products is  None:
        
#     return render(request, 'base/games.html', {'products': product})


def game_view(request):
    category = Category.objects.filter(name='Video Game').first()   
    if not category:
        return render(request, 'base/games.html', {'products': [], 'searched': 'Video Games', 'error': 'Category not found'})
    products = Product.objects.filter(category=category)
    return render(request, 'base/games.html', {'products': products, 'searched': 'Video Games'})


def console_view(request):
    category = Category.objects.filter(name='Console').first()    
    if not category:
        return render(request, 'base/console.html', {'products': [], 'searched': 'Console', 'error': 'Category not found'})
    products = Product.objects.filter(category=category)
    return render(request, 'base/console.html', {'products': products, 'searched': 'Console'})


def accessories_view(request):
    category = Category.objects.filter(name='Accessories').first()    
    if not category:
        return render(request, 'base/accessories.html', {'products': [], 'searched': 'Accessories', 'error': 'Category not found'})
    products = Product.objects.filter(category=category)
    return render(request, 'base/accessories.html', {'products': products, 'searched': 'Accessories'})



# @require_POST
# @login_required
# def add_to_wishlist(request):
#     product_id = request.POST.get('product_id')
#     product = get_object_or_404(Product, id=product_id)
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
#     if created:
#         return JsonResponse({'status': 'success', 'message': 'Product added to wishlist.'})
#     else:
#         return JsonResponse({'status': 'info', 'message': 'Product is already in your wishlist.'})

# @login_required
# def wishlist_display(request):
#     wishlist_items = Wishlist.objects.filter(user=request.user)
#     products = [item.product for item in wishlist_items]
#     for product in products:
#         print(product.name)

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

def search_bar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(name__contains=searched)
        return render(request, 'base/search_bar.html',
        {'searched':searched,
         'product':product})
        messages.success
    else:
        return render(request, 'base/search_bar.html',{})