from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls), # type: ignore
    path("", include("core.urls")),
    path("", include("userprofile.urls")),
    path("", include("story.urls")),
    path("notifications/", include("notifications.urls")),
]
