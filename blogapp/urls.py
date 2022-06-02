
from django.urls import path,include
from . import views

urlpatterns = [
    #path, name of function, namespace 
    path('',views.home),
    path('upload/',views.upload,name='upload'),
    path('update/<int:blog_id>',views.update_blog,name='update'),
    path('delete/<int:blog_id>',views.delete_blog,name='delete')
    
]