from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index, name='home' ),
    # path('r/', views.register),
    # path('ln/', views.login),
    # path('lo/', views.logout),
]
