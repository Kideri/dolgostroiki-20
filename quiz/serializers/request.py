from rest_framework import serializers


class AnswerQuestionRequestSerializer(serializers.Serializer):
    answers = serializers.ListSerializer(child=serializers.IntegerField(), required=True)
