from django.db import models


class Config(models.Model):
    level = models.PositiveIntegerField(unique=True)
    exp = models.PositiveBigIntegerField()
    description = models.CharField(max_length=2047, null=True, blank=False)

    @property
    def level_desc(self):
        if self.description:
            return self.description
        description = Config.objects.filter(level__lt=self.level, description__isnull=False).order_by('-level').last()
        return description.description
