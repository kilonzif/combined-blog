
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    #path, name of function, namespace 
    path('', views.home, name='home'),
    path('upload/',views.upload,name='upload'),
    path('update/<int:blog_id>',views.update_blog,name='update'),
    path('delete/<int:blog_id>',views.delete_blog,name='delete'),
    path('register', csrf_exempt(views.register), name="register"),
    path('login', csrf_exempt(auth_views.LoginView.as_view(template_name='auth/login.html')), name="login"),
    path('logout', csrf_exempt(auth_views.LogoutView.as_view(template_name='auth/logout.html')), name="logout")
]