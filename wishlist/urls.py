from django.urls import path
from . import views




urlpatterns = [
    path('', views.wishlist_view, name='wishlist_url'),
    # path('logout', views.logout_view, name='logout_url'),
    # path('register', views.register_view, name='register_url')
]