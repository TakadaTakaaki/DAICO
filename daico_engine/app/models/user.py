from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a email address')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)        
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    type_choices = {
        ('A', 'Client User'),
        ('B', 'Customer User')
    }
    user_type = models.CharField(
        max_length=1,
        choices=type_choices,
        default='B'
    )

    email = models.EmailField(max_length=128, unique=True)
    name = models.CharField(max_length=150, blank=True)
    sex_choices = {
        ('A', '男性'),
        ('B', '女性'),
        ('C', 'その他')
    }
    sex = models.CharField(
        max_length=1,
        choices=sex_choices,
        default=None,
        null=True
    )
    birth_year = models.IntegerField(
        max_length=4,
        default=None,
        null=True
    )
    birth_month = models.IntegerField(
        max_length=2,
        default=None,
        null=True
    )
    birth_day = models.IntegerField(
        max_length=2,
        default=None,
        null=True
    )
    address = models.CharField(
        max_length=300,
        default=None,
        null=True
    )
    phone = models.TextField(
        max_length=12,
        default=None,
        null=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
    class Meta:
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'
