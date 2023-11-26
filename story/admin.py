from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    """Admin View for Story"""

    list_display = ("title", "url", "created_by", "created_on", "reply_to")
    fields = ("title", "url", "content", "created_by", "reply_to")
    readonly_fields = ("created_by", "reply_to")

    search_fields = ("title", "url", "created_by", "created_on")
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
