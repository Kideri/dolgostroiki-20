from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User
from quiz.models import Question


class UserAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user')
    answers = ArrayField(models.IntegerField())
    score_received = models.FloatField()
