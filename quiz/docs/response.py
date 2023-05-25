from common.serializers import BaseResponseSerializer

from quiz.serializers import QuestionListSerializer, QuestionRetrieveSerializer, AnswerQuestionResponseSerializer


class QuestionListDocsSerializer(BaseResponseSerializer):
    result = QuestionListSerializer()


class QuestionRetrieveDocsSerializer(BaseResponseSerializer):
    result = QuestionRetrieveSerializer()


class AnswerQuestionDocsResponseSerializer(BaseResponseSerializer):
    result = AnswerQuestionResponseSerializer()
