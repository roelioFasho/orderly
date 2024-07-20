from django.shortcuts import render, redirect

# #the registration
# from .forms import RegistrationForm

# # login, logout
# from django.contrib.auth import authenticate, login, logout
# # Create your views here.

def index(request):
    return render(request, "base/home.html" )



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