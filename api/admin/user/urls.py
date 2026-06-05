from django.contrib import admin
from django.urls import path, include
from api.admin.common.views import CommonListAPIView

# ADMIN
urlpatterns = [

    path('list/', CommonListAPIView.as_view()),
]

# api/v1/admin/common/list/

#CRUD