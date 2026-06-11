from os import name

from api.site import views
from django.urls import path, include


urlpatterns = [
     path('', views.home, name='home'),
     path('contact/', views.contact, name='contact'),

     path('blog/',views.blog, name='blog'),
     path ('services/',views.services,name='services')

]


