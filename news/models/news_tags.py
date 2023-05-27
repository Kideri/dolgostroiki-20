from django.db import models

from .news import News
from .tag import Tag


class NewsTags(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='news')

    class Meta:
        unique_together = ("news", "tag")
