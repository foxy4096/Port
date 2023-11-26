from django.db import models
from django.contrib.auth.models import User
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


class Story(models.Model):
    title = models.CharField(max_length=512, help_text="Required")
    content = models.TextField(blank=True, null=True, help_text="Optional")
    url = models.URLField(null=True, blank=True, help_text="Optional")
    votes = models.ManyToManyField(User, related_name="votes")
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stories", blank=True, null=True
    )
    reply_to = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def vote(self, user):
        if user in self.votes.all():
            self.votes.remove(user)
            self.created_by.userprofile.decrease_karma()
            return self.notify_vote(user, "unvoted", False)
        else:
            self.votes.add(user)
            self.created_by.userprofile.increase_karma()
            return self.notify_vote(user, "voted", True)

    def notify_vote(self, user, verb, voted):
        Notification.notify(
            recipient=self.created_by,
            actor=user,
            verb=verb,
            object_id=self.id,
            object_type="story",
        )
        return voted

    def total_comments_count(self):
        f"""
        Count the total number of replies recursively for {self}
        """
        count = self.replies.count()
        count += sum(reply.total_comments_count() for reply in self.replies.all())
        return count
