from django.db import models


from .lesson import Lesson
from quiz.models import Question


class LessonQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='lesson')

    class Meta:
        unique_together = ("lesson", "question")
    