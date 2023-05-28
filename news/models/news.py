from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL


class News(models.Model):
    image = models.ImageField(upload_to="news/", null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    text = models.TextField(null=False, blank=False)

    def image_tag(self):
        return mark_safe(f'<img src="{MEDIA_URL}{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image preview'

    @property
    def tags_serialize(self):
        return [_.tag.id for _ in self.tags.all()]

    @property
    def shorten_text(self):
        return self.text[:255]

    class Meta:
        ordering = ['-id']
