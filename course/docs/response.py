from rest_framework import serializers
from common.serializers import BaseResponseSerializer


class ListCourseDocs(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    difficulty = serializers.IntegerField()
    tags = serializers.ListSerializer(child=serializers.IntegerField())
    total_lessons = serializers.IntegerField()
    free_lessons = serializers.IntegerField()
    lessons_passed = serializers.IntegerField()


class ListCourseDocsResponse(BaseResponseSerializer):
    result = serializers.ListSerializer(child=ListCourseDocs())


class LessonDocs(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    number = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_free = serializers.BooleanField()
    cost = serializers.IntegerField()
    duration = serializers.IntegerField()
    viewed = serializers.BooleanField()
    passed = serializers.BooleanField()


class RetrieveCourseDocs(ListCourseDocs):
    author_name = serializers.CharField(max_length=255)
    author_description = serializers.CharField()
    video = serializers.FileField()
    lessons = serializers.ListSerializer(child=LessonDocs())


class RetrieveCourseDocsResponse(BaseResponseSerializer):
    result = RetrieveCourseDocs()


class LessonResponseDocs(LessonDocs):
    questions = serializers.ListSerializer(child=serializers.IntegerField())


class RetrieveLessonDocsResponse(BaseResponseSerializer):
    result = LessonResponseDocs()
