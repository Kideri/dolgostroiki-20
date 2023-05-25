from django.urls import path

from quiz.views import (
    QuestionListView,
    QuestionRetrieveView,
    QuestionAnswerView
)

urlpatterns = [
    path("", QuestionListView.as_view(), name="question_list"),
    path("<int:question_id>", QuestionRetrieveView.as_view(), name="question_retrieve"),
    path("<int:question_id>/answer", QuestionAnswerView.as_view(), name="question_answer"),
]
