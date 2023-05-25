from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    text = models.CharField(max_length=8092, null=False, blank=False)

    class Meta:
        ordering = ['-id']
