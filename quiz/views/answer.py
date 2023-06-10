from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from quiz.docs import AnswerQuestionDocsResponseSerializer
from quiz.models import Question, UserAnswers
from course.models import UserPassedLessons
from quiz.serializers import (
    AnswerQuestionResponseSerializer,
    AnswerQuestionRequestSerializer
)


class QuestionAnswerView(BaseAPIView):
    request_serializer = AnswerQuestionRequestSerializer
    response_serializer = AnswerQuestionResponseSerializer
    question_id = None

    @swagger_auto_schema(
        responses={200: AnswerQuestionDocsResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=AnswerQuestionRequestSerializer(),
        tags=["Question"],
        operation_id="Answer question",
    )
    def post(self, request, question_id: int = None):
        self.question_id = question_id
        return self.base_method()

    def get_result(self):
        object_ = Question.objects.filter(id=self.question_id)

        if not object_.exists():
            raise CustomException("question not found")

        object_ = object_.first()

        if UserAnswers.objects.filter(user=self.request.user, question=object_).exists():
            raise CustomException("question already answered")

        score = 0
        bad_score = 0

        correct_answers = [_.id for _ in object_.answers.filter(is_correct=True).all()]
        user_answers = self.get_data_from_request().data.get('answers')

        for ans in user_answers:
            score += int(ans in correct_answers)
            bad_score += int(ans not in correct_answers)

        score = round(score / (len(correct_answers) + bad_score), 3)
        reaction = object_.correct_answer_reaction if score == 1 else object_.incorrect_answer_reaction

        level = self.request.user.user_current_level
        level.total_exp += int(object_.score * score)
        level.process_level()

        UserAnswers.objects.create(
            user=self.request.user,
            question=object_,
            answers=user_answers,
            score_received=score,
        )

        if object_.lesson.exists():
            for q_lesson in object_.lesson.all():
                UserPassedLessons.objects.create(
                    user=self.request.user,
                    lesson=q_lesson.lesson
                )

        return self.response_serializer(
            {'score': score, 'answers': object_.correct_answers_retrieve, 'reaction': reaction}
        ).data
