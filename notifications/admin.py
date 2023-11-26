from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin View for Notification"""

    list_display = (
        "actor",
        "verb",
        "recipient",
        "object_type",
        "object_id",
        "created_at",
    )

    list_per_page = 20
