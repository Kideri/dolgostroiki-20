# from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models

from .course_model import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    number = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=255)

    is_free = models.BooleanField(default=True)
    cost = models.IntegerField(validators=[MinValueValidator(1)])
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    # images = ArrayField(base_field=models.ImageField(), null=True, blank=True)
    # videos = ArrayField(base_field=models.URLField(), null=True, blank=True)

    class Meta:
        unique_together = ("course", "number")

    @property
    def lessons_questions(self):
        return [_.question.id for _ in self.questions.all()]
