from django.contrib import admin
from news.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title", )
    list_display_links = ("title", )
    search_fields = ("title", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "background_color"
                )
            },
        ),
    )
