from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from quiz.docs import QuestionRetrieveDocsSerializer
from quiz.models import Question
from quiz.serializers import (
    QuestionRetrieveSerializer
)


class QuestionRetrieveView(BaseAPIView):
    response_serializer = QuestionRetrieveSerializer
    question_id = None

    @swagger_auto_schema(
        responses={200: QuestionRetrieveDocsSerializer(), 401: BaseResponseSerializer()},
        tags=["Question"],
        operation_id="Get question",
    )
    def get(self, request, question_id: int = None):
        self.question_id = question_id
        return self.base_method()

    def get_result(self):
        object_ = Question.objects.filter(id=self.question_id)
        if not object_.exists():
            raise CustomException("question not found")
        object_ = object_.first()
        return self.response_serializer(object_).data
