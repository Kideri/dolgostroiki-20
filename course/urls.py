from django.urls import path

from course.views import (
    CourseListView,
    CourseRetrieveView,
    LessonRetrieveView,
)

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<int:course_id>", CourseRetrieveView.as_view(), name="course_retrieve"),
    path("lesson/<int:lesson_id>", LessonRetrieveView.as_view(), name="lesson_retrieve"),
]
