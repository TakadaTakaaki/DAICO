from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from app.models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'name',)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'sex', 'birth_year', 'birth_month','birth_day', 'address', 'phone')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる