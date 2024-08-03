
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_view , name='cartview_url'),
    path('add/', views.cart_add , name='cart_add_url'),
    path('delete/', views.cart_delete , name='cart_delete_url'),
    path('update/', views.cart_update , name='cart_update_url'),



]

