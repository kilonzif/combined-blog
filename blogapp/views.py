from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import BlogCreate, UserRegisterForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import json
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.

@login_required
def home(request):
    blogs = BlogPost.objects.all()
    return render(request,'blogapp/index.html',{'blogs':blogs})
    
def upload(request):
    upload=BlogCreate()
    if request.method=='POST':
        upload=BlogCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'blogapp/upload_form.html',{'upload':upload})

def update_blog(request,blog_id):
    blog_id=int(blog_id)
    try:
     blog_up=BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        return redirect('home')
    blog_form=BlogCreate(request.POST or None,instance=blog_up)
    if blog_form.is_valid():
        blog_form.save()
        return redirect('home')
    return render (request,'blogapp/upload_form.html',{'upload':blog_form})

def delete_blog(request,blog_id):
     
    blog_id=int(blog_id)
    try:
        blog_up=BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        return redirect('blogapp/index.html')
    blog_up.delete()
    return redirect('blogapp/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            emailval = form.cleaned_data.get('email')
            usersname = form.cleaned_data.get('username')
            domain = get_current_site(request).domain
            link = reverse('login')
            loginurl = 'http://'+domain+link
            
            email = EmailMessage(
                f'Hi {usersname}, Welcome to The Blog App!',
                f'Start your The Bloging journey here: {loginurl}',
                'parehoy488@iconzap.com',
                [f'{emailval}']
            )
            email.send()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')
    else:        
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})
            