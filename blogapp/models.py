from contextlib import nullcontext
from datetime import datetime
from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Tag(models.Model):    
    name =models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blogImages',blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',null=True)
    bio = models.TextField()

    def __str__(self):
        return self.user

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)


    def __str__(self):
        return self.content

