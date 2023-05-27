from django.db import models
from .user import User
from .preference import Preference


class UserPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE, related_name='user')

    class Meta:
        unique_together = ("user", "preference")

    def __str__(self):
        return self.preference.name
