from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    background_color = ColorField(default='#000000')

