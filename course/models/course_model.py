from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL


class Course(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_description = models.TextField()
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to="question/", null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{MEDIA_URL}{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image preview'

    @property
    def course_tags(self):
        return [_.tag.id for _ in self.tags.all()]

    @property
    def total_lessons(self):
        return self.lessons.count()

    @property
    def free_lessons(self):
        return self.lessons.filter(is_free=True).count()
