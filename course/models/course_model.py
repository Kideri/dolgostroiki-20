from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL


class Course(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_description = models.TextField()
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    video = models.FileField(
        upload_to='course/videos/', null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
            )
        ]
    )

    def video_tag(self):
        return mark_safe(f'<video src="{MEDIA_URL}{self.video}" width="150" height="150" />')

    video_tag.short_description = 'Video preview'

    @property
    def course_tags(self):
        return [_.tag.id for _ in self.tags.all()]

    @property
    def total_lessons(self):
        return self.lessons.count()

    @property
    def free_lessons(self):
        return self.lessons.filter(is_free=True).count()
