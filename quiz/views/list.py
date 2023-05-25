from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from quiz.docs import QuestionListDocsSerializer
from quiz.models import Question
from quiz.serializers import (
    QuestionListSerializer
)


class QuestionListView(BaseAPIView):
    response_serializer = QuestionListSerializer

    @swagger_auto_schema(
        responses={200: QuestionListDocsSerializer(), 401: BaseResponseSerializer()},
        tags=["Question"],
        operation_id="Get questions list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Question.objects.all()]
