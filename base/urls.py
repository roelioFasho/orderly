from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index, name='home' ),
    path('product',views.product_view, name='product' ),
    path('wishlist/',views.wish_view, name='wishlist' ),
    path('abc/',views.product_view2, name='prove' ),
    path('privacy-policy/',views.privacy_policy_view, name='privacy-policy' ),
    path('terms-of-service/',views.terms_service_view, name='terms-of-service' ),
    # path('search-bar/',views.search_bar, name='search-bar' ),

]
