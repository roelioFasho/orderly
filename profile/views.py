from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# # from django.http import HttpResponse




def login_view(request):
    if request.method == 'POST': # if user fills out the form 'take' username and password
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')

        else:
            messages.error(request, 'there was an error' )
            return redirect('login_page')
    else:
        return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home_page')
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'authentication/register.html', context)



