from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    text = models.TextField(null=False, blank=False)

    @property
    def tags_serialize(self):
        return [_.tag.id for _ in self.tags.all()]

    @property
    def shorten_text(self):
        return self.text[:255]

    class Meta:
        ordering = ['-id']
