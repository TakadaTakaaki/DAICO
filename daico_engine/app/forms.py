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
        fields = ('foo','date','name','message',)
        labels = {'foo': 'お問い合わせ種類','date': '日付','name': '名前','message': '返信内容'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '代行エンジン'}),
            'message': forms.TextInput(attrs={'placeholder': '返信内容'}),
        }
        
# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('email', 'name', 'foo', 'message', 'phone')
#         labels = {'email': 'メールアドレス','name': '名前','foo': 'お問い合わせ種類','message': 'お問い合わせ内容','phone': '電話番号',}
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': '例) 代行　エンジン'}),
#             'email': forms.TextInput(attrs={'placeholder': '例) neekey@gmail.com'}),
#             'message': forms.TextInput(attrs={'placeholder': '例) パスワードを忘れてしまいました'}),
#             'phone': forms.TextInput(attrs={'placeholder': '例) 09065668268'}),
#         }