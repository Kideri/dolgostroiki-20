from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from course.docs import RetrieveLessonDocsResponse
from course.models import Lesson, UserPassedLessons, UserViewedLessons
from course.serializers import (
    LessonResponseSerializer
)


class LessonRetrieveView(BaseAPIView):
    response_serializer = LessonResponseSerializer
    lesson_id = None

    @swagger_auto_schema(
        responses={200: RetrieveLessonDocsResponse(), 401: BaseResponseSerializer()},
        tags=["Course"],
        operation_id="Get lesson",
    )
    def get(self, request, lesson_id: int = None):
        self.lesson_id = lesson_id
        return self.base_method()

    def get_result(self):
        object_ = Lesson.objects.filter(id=self.lesson_id)

        if not object_.exists():
            raise CustomException("lesson not found")

        object_ = object_.first()

        data = self.response_serializer(object_).data

        data.update({
            "viewed": UserViewedLessons.objects.filter(user=self.request.user, lesson=object_),
            "passed": UserPassedLessons.objects.filter(user=self.request.user, lesson=object_),
        })

        return data
