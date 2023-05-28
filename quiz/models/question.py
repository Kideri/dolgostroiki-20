from django.db import models
from django.utils.html import mark_safe
from source.settings import MEDIA_URL


class Question(models.Model):
    image = models.ImageField(upload_to="question/", null=True, blank=True)
    question = models.CharField(max_length=2047, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    score = models.PositiveIntegerField(default=1)
    correct_answer_reaction = models.CharField(max_length=2047, null=True, blank=True)
    incorrect_answer_reaction = models.CharField(max_length=2047, null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{MEDIA_URL}{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image preview'

    @property
    def answers_retrieve(self):
        return [{'id': _.id, 'text': _.text} for _ in self.answers.all()]

    @property
    def correct_answers_retrieve(self):
        return [{'id': _.id, 'text': _.text} for _ in self.answers.filter(is_correct=True).all()]
