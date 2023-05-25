from django.db import models


class Target(models.Model):
    code = models.CharField(max_length=31, null=False, blank=False, help_text='Name for server', primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, help_text='Name for user')

    def __str__(self):
        return f"{self.code} | {self.name}"
