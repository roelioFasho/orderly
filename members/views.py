from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            message = messages.success(request, f"Welcome {username}!")
            return redirect('home')
            
            
        else:
            message = messages.error(request, "Try again!")
            # Return an 'invalid login' error message.  
            return redirect('login')
        
    
    else:

        return render(request, 'members/login.html')




def logout_view(request):
    logout(request)
    messages.success(request, "You have been logout!")
    return redirect('home')

def register_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You were sucesfully registered {username}")
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'members/register.html', context)

