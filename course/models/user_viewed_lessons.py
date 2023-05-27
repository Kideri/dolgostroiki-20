from django.db import models

from .lesson import Lesson
from user.models import User


class UserViewedLessons(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewed_lessons')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "lesson")
