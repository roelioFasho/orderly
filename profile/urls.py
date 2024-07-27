from django.urls import path, include
from . import  views

# # Create your views here.

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path("login/", views.login_view, name='login')

]





