from django.shortcuts import render, redirect
from .models import Product

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



def product_view(request):
    return render(request, "base/product.html")

def product_view2(request):
    product = Product.objects.filter()
    return render(request, "base/login.html", {'products':product})

def wish_view(request):
    return render(request, "base/wishlist.html" )


def privacy_policy_view(request):
    return render(request, "base/privacy_policy.html" )
def terms_service_view(request):
    return render(request, "base/terms_of_service.html" )
# def register(request):
#     pass
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         return redirect('home-page')
    # else:
    #     form = RegistrationForm()
    
    # context = {'form': form}
    # return render(request, 'base/register.html', context)



# def login_func(request):
#     return redirect(request, "base/login.html", {})

# def logout_func(request):
#     pass