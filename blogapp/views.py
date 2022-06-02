from pickletools import decimalnl_long
from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import BlogCreate
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home(request):
    blogs=BlogPost.objects.all()
    return render (request,'index.html',{'blogs':blogs})
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
        return render(request,'upload_form.html',{'upload':upload})

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
    return render (request,'upload_form.html',{'upload':blog_form})

def delete_blog(request,blog_id):
     
    blog_id=int(blog_id)
    try:
        blog_up=BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        return redirect('home')
    blog_up.delete()
    return redirect('home')

