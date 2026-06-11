from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    # path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', include('api.site.urls')),

    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),


]


