# from django.contrib import admin
# from .models import post
from django.contrib import admin
from .models import Article, Category, User, Company_data, Plan, Staff
# from django.contrib.auth.admin import UserAdmin
# from .forms import UserCreationForm, UserChangeForm

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Company_data)
admin.site.register(Plan)
admin.site.register(Staff)

# class UserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = User
#     list_display = ['email', 'username',]
