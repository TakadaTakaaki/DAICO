# from django.contrib import admin
# from .models import post
from django.contrib import admin
from .models import Post
from .models import Category
from .models import Company_data
from .models import Staff
from .models import Plan

admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Company_data)

admin.site.register(Staff)

admin.site.register(Plan)