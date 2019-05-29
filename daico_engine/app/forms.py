# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django import forms
from django.forms import ModelForm
from .models import Chat

# class UserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('email', 'name', 'user_type')

# class UserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email', 'name', 'password', 'sex', 'birth_year', 'birth_month',
#                   'birth_day', 'address', 'phone')

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ('message',)
        labels = {'message': '返信内容'}
        widgets = {'message': forms.TextInput(attrs={'placeholder': '返信内容'})}
        