from django.urls import path
from . import  views
urlpatterns = [
    path('karimpdh/',views.index ),
    path('karimpdhlali/',views.index2 ),
]
