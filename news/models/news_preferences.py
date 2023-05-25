from django.db import models

from .news import News
from user.models import Preference


class NewsPreferences(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='preferences')
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE, related_name='news')
