from rest_framework import serializers

from quiz.models import Question


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question",
        )
        ref_name = "question_list_result"


class QuestionAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField(max_length=255)


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    answers = serializers.ListSerializer(
        child=QuestionAnswerSerializer(),
        source="answers_retrieve"
    )

    class Meta:
        model = Question
        fields = (
            "id",
            "image",
            "question",
            "text",
            "answers",
        )
        ref_name = "question_retrieve_result"


class AnswerQuestionResponseSerializer(serializers.Serializer):
    score = serializers.FloatField()
    answers = serializers.ListSerializer(
        child=QuestionAnswerSerializer()
    )
    reaction = serializers.CharField(max_length=255)
