from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=2047, null=False, blank=False)
    correct_answer_reaction = models.CharField(max_length=2047, null=True, blank=True)
    incorrect_answer_reaction = models.CharField(max_length=2047, null=True, blank=True)

    @property
    def answers_retrieve(self):
        return [{'id': _.id, 'text': _.text} for _ in self.answers.all()]

    @property
    def correct_answers_retrieve(self):
        return [{'id': _.id, 'text': _.text} for _ in self.answers.filter(is_correct=True).all()]
