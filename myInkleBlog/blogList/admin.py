from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(BlogPost, PostAdmin)
