from django.urls import path
from . import  views


urlpatterns = [
    path('',views.index, name='home' ),
    path('privacy-policy/',views.privacy_policy_view, name='privacy-policy' ),
    path('terms-of-service/',views.terms_service_view, name='terms-of-service' ),
    path('product/<str:name>/', views.product_view, name='product_view1'),
    path('search-bar/',views.search_bar, name='search-bar'),
    path('games/', views.game_view, name='games_url'),
    path('console/', views.console_view, name='console_url'),
    path('accessories/', views.accessories_view, name='accessories_url'),
    path('rolep/', views.rolep_view, name='rolep_url'),
    path('singlep/', views.singlep_view, name='singlep_url'),
    path('multip/', views.multip_view, name='multip_url'),
    path('merch/', views.merch_view, name='merch_url'),
]



