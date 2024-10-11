from django.contrib import admin
from django.urls import path, include

API_BASE_PATH = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_BASE_PATH}cron/", include("cronApp.urls")),
    path(f"{API_BASE_PATH}fetch/", include("fetchApp.urls")),
]
