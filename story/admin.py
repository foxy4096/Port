from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    '''Admin View for Story'''

    list_display = ('title', 'url', 'created_by', 'created_on')
    fields = ('title', 'url', 'created_by')
    readonly_fields = ('created_by',)

    search_fields = ('title', 'url', 'created_by', 'created_on')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

