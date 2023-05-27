from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from course.docs import ListCourseDocsResponse
from course.models import Course, UserPassedLessons
from course.serializers import (
    ListCourseResponse
)


class CourseListView(BaseAPIView):
    response_serializer = ListCourseResponse

    @swagger_auto_schema(
        responses={200: ListCourseDocsResponse(), 401: BaseResponseSerializer()},
        tags=["Course"],
        operation_id="Get courses list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        result = []
        for obj in Course.objects.all():
            data = self.response_serializer(obj).data
            data.update({
                "lessons_passed": UserPassedLessons.objects.filter(user=self.request.user, lesson__course=obj).count()
            })
        return result
