from django.db import models

from news.models import Tag
from .course_model import Course


class CourseTag(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
