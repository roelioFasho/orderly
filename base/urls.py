from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index, name='home' ),
    path('abc/',views.product_view2, name='prove' ),
    path('privacy-policy/',views.privacy_policy_view, name='privacy-policy' ),
    path('terms-of-service/',views.terms_service_view, name='terms-of-service' ),
    path('product/<str:name>/', views.product_view, name='product_view1'),
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_display, name='wishlist_display1'),
    # path('wishlist/<int:id>/', views.wishlist_view, name='wishlist1'),

    # path('search-bar/',views.search_bar, name='search-bar' ),

]



