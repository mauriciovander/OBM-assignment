
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),    
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    # path('auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]