from django.contrib import admin
from django.urls import path, include
from .views import ProductListAPIView, CarListAPIView

# ADMIN
urlpatterns = [

    path('list/', ProductListAPIView.as_view()),
    path('list1/',CarListAPIView.as_view()),

]
#api/v1/admin/common/list/