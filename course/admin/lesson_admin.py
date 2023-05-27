from django.contrib import admin
from course.models import Lesson, LessonQuestion


class QuestionInline(admin.TabularInline):
    model = LessonQuestion


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
    list_display = ("name", )
    list_display_links = ("name", )
    search_fields = ("name", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "course",
                    "name",
                    "number",
                    "duration",
                )
            },
        ),
        (
            "Paid section",
            {
                "fields": (
                    "is_free",
                    "cost",
                )
            }
        ),
        # (
        #     "External section",
        #     {
        #         "fields": (
        #             "images",
        #             "videos",
        #         )
        #     }
        # )
    )
