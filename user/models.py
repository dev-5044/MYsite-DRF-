from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from user.managers import CustomUserManager



class Customer(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, verbose_name='телефон')
    avatar = models.ImageField(upload_to='user_foto', verbose_name='аватар',
                               default='images.png', blank=True)
    website = models.URLField(blank=True, verbose_name='сайт')
    country = models.CharField(max_length=100, verbose_name='страна', blank=True)
    city = models.CharField(max_length=50, verbose_name='город', blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    objects = CustomUserManager()

    REQUIRED_FIELD = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

