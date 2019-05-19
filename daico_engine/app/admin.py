# from django.contrib import admin
# from .models import post
from django.contrib import admin
from .models import Post
from .models import Category
from .models import Company_data

admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Company_data)