from django.contrib import admin
from django.urls import path, include

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# ADMIN
urlpatterns = [

    path('common/', include('api.admin.common.urls')),
    # path('user/', include('api.admin.user.urls'))

]
