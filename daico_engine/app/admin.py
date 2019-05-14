# from django.contrib import admin
# from .models import post
from django.contrib import admin
from .models import Post
from .models import Category

admin.site.register(Post)

admin.site.register(Category)
# class postadmin(admin.Modelpost):
    # ordering = ['id']
# idの昇順でソート
    # list_display = ['id', 'name']
# リストで表示するフィールド


# Register your models here.
