from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL

from .course_model import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    number = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=255)
    description = models.TextField()

    is_free = models.BooleanField(default=True)
    cost = models.IntegerField(validators=[MinValueValidator(1)])
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="question/", null=True, blank=True)
    video = models.FileField(
        upload_to='lesson/videos/', null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
            )
        ]
    )

    def video_tag(self):
        return mark_safe(f'<video src="{MEDIA_URL}{self.video}" width="150" height="150" />')

    video_tag.short_description = 'Video preview'

    def image_tag(self):
        return mark_safe(f'<img src="{MEDIA_URL}{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image preview'

    class Meta:
        unique_together = ("course", "number")

    @property
    def lessons_questions(self):
        return [_.question.id for _ in self.questions.all()]
