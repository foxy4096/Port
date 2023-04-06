from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    karma = models.IntegerField(default=0)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def increase_karma(self, amount=1):
        self.karma += amount
        self.save()

    def decrease_karma(self, amount=1):
        self.karma -= amount
        self.save()
