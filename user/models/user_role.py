from django.db import models


class UserRole(models.TextChoices):
    default = ("D", "Default")
    moderator = ("M", "Moderator")
