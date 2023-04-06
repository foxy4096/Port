
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver

from django.contrib.auth.models import User
from .models import Story


@receiver(post_save, sender=Story)
def create_story(sender, instance:Story, created, **kwargs):
    if created:
        instance.created_by.userprofile.increase_karma()

@receiver(post_delete, sender=Story)
def delete_story(sender, instance:Story, **kwargs):
    instance.created_by.userprofile.decrease_karma()
