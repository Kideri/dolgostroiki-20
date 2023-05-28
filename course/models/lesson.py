from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL

from .course_model import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    number = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=255)

    is_free = models.BooleanField(default=True)
    cost = models.IntegerField(validators=[MinValueValidator(1)])
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="question/", null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{MEDIA_URL}{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image preview'

    class Meta:
        unique_together = ("course", "number")

    @property
    def lessons_questions(self):
        return [_.question.id for _ in self.questions.all()]
