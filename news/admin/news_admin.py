from django.contrib import admin
from news.models import News, NewsPreferences


class PreferenceInline(admin.TabularInline):
    model = NewsPreferences


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        PreferenceInline,
    ]
    list_display = ("title", )
    list_display_links = ("title", )
    search_fields = ("title", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                )
            },
        ),
        (
            "Text",
            {
                "fields": (
                    "text",
                )
            }
        )
    )
