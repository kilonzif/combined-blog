from .models import BlogPost, Profile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BlogCreate(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields='__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']