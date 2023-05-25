from django.contrib import admin
from user.models import Preference


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
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
