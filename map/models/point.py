from django.db import models


class Point(models.Model):
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)

    name = models.CharField(max_length=255)
    description = models.TextField()

    work_time = models.CharField(max_length=2047)
