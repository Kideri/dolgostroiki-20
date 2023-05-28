from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from course.docs import RetrieveCourseDocsResponse
from course.models import Course, UserPassedLessons, UserViewedLessons
from course.serializers import (
    RetrieveCourseResponse
)


class CourseRetrieveView(BaseAPIView):
    response_serializer = RetrieveCourseResponse
    course_id = None

    @swagger_auto_schema(
        responses={200: RetrieveCourseDocsResponse(), 401: BaseResponseSerializer()},
        tags=["Course"],
        operation_id="Get course",
    )
    def get(self, request, course_id: int = None):
        self.course_id = course_id
        return self.base_method()

    def get_result(self):
        object_ = Course.objects.filter(id=self.course_id)

        if not object_.exists():
            raise CustomException("course not found")

        object_ = object_.first()

        data = self.response_serializer(object_).data

        data.update({
            "lessons_passed": UserPassedLessons.objects.filter(user=self.request.user, lesson__course=object_).count()
        })

        for lesson in data["lessons"]:
            lesson.update({
                "viewed": UserViewedLessons.objects.filter(user=self.request.user, lesson_id=lesson["id"]).exists(),
                "passed": UserPassedLessons.objects.filter(user=self.request.user, lesson_id=lesson["id"]).exists(),
            })

        return data
