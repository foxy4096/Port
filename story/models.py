from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=512, help_text="required")
    content = models.TextField(blank=True, null=True, help_text="optional")
    url = models.URLField(null=True, blank=True, help_text="optional")
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
            self.save()
            return False
        else:
            self.votes.add(user)
            self.created_by.userprofile.increase_karma()
            self.save()
            return True
