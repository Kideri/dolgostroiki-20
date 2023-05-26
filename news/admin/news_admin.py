from django.contrib import admin
from news.models import News, NewsPreferences, NewsTags


class PreferenceInline(admin.TabularInline):
    model = NewsPreferences


class TagsInline(admin.TabularInline):
    model = NewsTags


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        PreferenceInline, TagsInline
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
