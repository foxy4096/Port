from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Userprofile


class UserprofileInline(admin.StackedInline):
    """
    Including the userprofile model in the user model by inline admin
    """

    model = Userprofile
    readonly_fields = [
        "karma",
    ]
    fields = [
        "karma",
        "about",
    ]
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """
    Adding the profile inline in user model admin
    """

    inlines = [
        UserprofileInline,
    ]


# Registering the model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)