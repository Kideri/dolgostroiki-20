from django.db import models
from .point import Point
from user.models import Preference


class PointPreference(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='preferences')
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE, related_name='points')

    class Meta:
        unique_together = ("point", "preference")
