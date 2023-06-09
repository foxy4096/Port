from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from django.contrib.auth.models import User
from .models import Userprofile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance).increase_karma()
