from django.contrib import admin

from .models import BlogPost,Comment,Tag,Profile


admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)
