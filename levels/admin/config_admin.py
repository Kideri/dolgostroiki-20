from django.contrib import admin
from levels.models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("level", )
    list_display_links = ("level", )
    search_fields = ("level", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "level",
                    "exp",
                    "description"
                )
            },
        ),
    )
