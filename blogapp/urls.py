
from django.urls import path,include
from . import views

urlpatterns = [
    #path, name of function, namespace 
    path('',views.home)
    
]