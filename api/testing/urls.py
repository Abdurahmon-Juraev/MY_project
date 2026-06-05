
from django.contrib import admin
from django.urls import path, include
#from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# TESTING
urlpatterns = [
     path('v1/admin/', include('api.admin.urls')),
     path('v1/site/', include('api.site.urls')),
     path('v1/testing/', include('api.testing.urls'))

]


