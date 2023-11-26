from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    recipient = models.ForeignKey(
        User, related_name="notifications", on_delete=models.CASCADE
    )
    actor = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    object_type = models.CharField(max_length=255)
    object_id = models.PositiveBigIntegerField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.recipient}'s {self.object_type}."

    class Meta:
        ordering = ["is_read", "-created_at"]

    @staticmethod
    def notify(recipient, actor, verb, object_type, object_id):
        """
        Create a new notification to be sent to the recipient.
        """
        if recipient != actor:
            return Notification.objects.get_or_create(
                recipient=recipient,
                actor=actor,
                verb=verb,
                object_type=object_type,
                object_id=object_id
            )[0]