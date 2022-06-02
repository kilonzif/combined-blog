from socket import fromshare
from django import forms
from .models import BlogPost
class BlogCreate(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields='__all__'
      