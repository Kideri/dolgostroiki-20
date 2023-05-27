from django.contrib import admin
from quiz.models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    list_display = ("question", )
    list_display_links = ("question", )
    search_fields = ("question", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "question",
                    "text",
                )
            },
        ),
        (
            "Reactions",
            {
                "fields": (
                    "correct_answer_reaction",
                    "incorrect_answer_reaction"
                )
            }
        )
    )
