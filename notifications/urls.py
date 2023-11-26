from django.urls import path

from . import views

urlpatterns = [
    path("", views.notification_page, name="notification_page"),
    path(
        "<int:id>/",
        views.notification_redirect,
        name="notification_redirect",
    ),
]
