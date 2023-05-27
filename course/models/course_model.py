from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_description = models.TextField()
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    @property
    def course_tags(self):
        return [_.tag.id for _ in self.tags.all()]

    @property
    def total_lessons(self):
        return self.lessons.count()

    @property
    def free_lessons(self):
        return self.lessons.filter(is_free=True).count()
