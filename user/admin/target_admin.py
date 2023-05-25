from django.contrib import admin
from user.models import Target


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name"
    )
    list_display_links = ("code", )
    search_fields = ("code", "name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "code",
                    "name",
                )
            },
        ),
    )
