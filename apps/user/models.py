from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.fields import CharField, ImageField

from apps.user.apps import UserConfig


class User(AbstractUser):
    name =models. max_length=100
    email =models.CharField(max_length=100)
    phone_number= models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)





