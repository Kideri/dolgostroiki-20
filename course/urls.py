from django.urls import path

from course.views import (
    CourseListView,
    CourseRetrieveView,
)

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<int:course_id>", CourseRetrieveView.as_view(), name="course_retrieve"),
]
