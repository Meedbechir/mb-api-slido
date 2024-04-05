from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Slido Project",
      default_version='v1',
      description="Slido is a project where we can create survey, share them and invite friends to join",
      terms_of_service="https://www.yourproject.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.com"),
      license=openapi.License(name="Your Project License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/', include('sondage_one.urls')),
    path('api/sondage_two/', include('sondage_two.urls')),
   #  path('api/sondage_three/', include('sondage_three.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]