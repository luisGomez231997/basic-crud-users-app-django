"""app URL Configuration"""
from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Basic App API",
      default_version='v1.',
      description="Api to manage the information to users system.",
      terms_of_service="",
      contact=openapi.Contact(email="luis.alberto.gomez@correounivalle.edu.co"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/admin-app/', admin.site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
