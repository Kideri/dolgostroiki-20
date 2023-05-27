from rest_framework import serializers

from common.serializers import BaseResponseSerializer

from quiz.serializers import QuestionListSerializer, AnswerQuestionResponseSerializer


class QuestionListDocsSerializer(BaseResponseSerializer):
    result = QuestionListSerializer()


class QuestionAnswerDocsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField(max_length=255)


class QuestionRetrieveSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=2047)
    text = serializers.CharField()
    answers = serializers.ListSerializer(child=QuestionAnswerDocsSerializer())
    user_answers = serializers.ListSerializer(child=serializers.IntegerField(), required=False)

    class Meta:
        ref_name = 'q_retrieve_docs_serializer'


class QuestionRetrieveDocsSerializer(BaseResponseSerializer):
    result = QuestionRetrieveSerializer()


class AnswerQuestionDocsResponseSerializer(BaseResponseSerializer):
    result = AnswerQuestionResponseSerializer()
