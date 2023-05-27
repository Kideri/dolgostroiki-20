from django.db import models
from .user import User
from .target import Target


class UserTargets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targets')
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='user')

    class Meta:
        unique_together = ("user", "target")

    def __str__(self):
        return self.target.name
