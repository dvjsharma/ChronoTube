from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="ChronoTube",
      default_version='v1',
      description="API to retrieve the latest YouTube videos based on specific tags or search queries",
      contact=openapi.Contact(email="divijs75@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

API_BASE_PATH = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_BASE_PATH}cron/", include("cronApp.urls")),
    path(f"{API_BASE_PATH}fetch/", include("fetchApp.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
