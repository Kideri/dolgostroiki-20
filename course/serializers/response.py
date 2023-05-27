from rest_framework import serializers
from course.models import Course, Lesson


class ListCourseResponse(serializers.ModelSerializer):
    tags = serializers.ListSerializer(child=serializers.IntegerField(), source="course_tags")
    total_lessons = serializers.IntegerField(source="total_lessons")
    free_lessons = serializers.IntegerField(source="free_lessons")

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "difficulty",
            "tags",
            "total_lessons",
            "free_lessons",
        )
        ref_name = "course_list_result"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "number",
            "name",
            "is_free",
            "cost",
            "duration"
        )
        ref_name = "lesson_get_result"


class RetrieveCourseResponse(ListCourseResponse):
    lessons = serializers.ListSerializer(child=LessonSerializer())

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "difficulty",
            "tags",
            "total_lessons",
            "free_lessons",
            "lessons"
        )
        ref_name = "course_list_result"

