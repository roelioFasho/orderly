from django.shortcuts import render, redirect
from .models import Product
from django.shortcuts import get_object_or_404

# #the registration
# from .forms import RegistrationForm

# # login, logout
# from django.contrib.auth import authenticate, login, logout
# # Create your views here.

# def search_bar(request): 
#     if request.method == "POST":
#         searched = request.POST['searched']
        
#         return render(request, 'base/search_bar.html',
#         {'searched':searched})
#     else:
#         return render(request, 'base/search_bar.html',{} )

def index(request):
    product = Product.objects.filter()
    return render(request, "base/home.html", {'products':product} )



def product_view(request, name):
    product = Product.objects.get(name=name)
    return render(request, "base/product.html", {'product':product})



def product_view2(request):
    product = Product.objects.filter()
    return render(request, "base/login.html", {'products':product})

def wish_view(request):
    return render(request, "base/wishlist.html" )


def privacy_policy_view(request):
    return render(request, "base/privacy_policy.html" )


def terms_service_view(request):
    return render(request, "base/terms_of_service.html" )
