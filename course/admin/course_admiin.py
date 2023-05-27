from django.contrib import admin
from course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_display_links = ("name", )
    search_fields = ("name", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "difficulty",
                )
            },
        ),
        (
            "Author section",
            {
                "fields": (
                    "author_name",
                    "author_description",
                )
            }
        )
    )
