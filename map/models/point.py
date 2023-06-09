from django.db import models


class Point(models.Model):
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)

    name = models.CharField(max_length=255)
    description = models.TextField()

    work_time = models.CharField(max_length=2047, null=True, blank=True)
    address = models.CharField(max_length=2047, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
