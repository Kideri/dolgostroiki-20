from django.contrib import admin
from course.models import Course, CourseTag


class TagInline(admin.TabularInline):
    model = CourseTag


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_display = ("name", )
    list_display_links = ("name", )
    search_fields = ("name", )
    readonly_fields = ("video_tag", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "difficulty",
                    "video_tag",
                    "video",
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
