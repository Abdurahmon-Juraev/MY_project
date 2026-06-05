from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.db.models.fields import TextField
from rest_framework.fields import CharField, ImageField

from apps.user.models import User


# # Create your models here.
# class Common(models.Model):
#     title = models.CharField(max_length=250)
#     text = models.TextField()
#     int = models.PositiveIntegerField()
#     float = models.FloatField()

class Category(models.Model):
    name =TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_products")
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products %Y/%m/%d/', null=True, blank=True )
    category = ForeignKey(Category, on_delete=models.CASCADE, related_name="products")


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products %Y/%m/%d/', null=True, blank=True)




