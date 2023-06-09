from django.contrib import admin
from map.models import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ("name", "longitude", "latitude")
    list_display_links = ("name", )
    search_fields = ("name", "longitude", "latitude")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "work_time",
                    "address",
                    "phone_number",
                )
            },
        ),
        (
            "Map position",
            {
                "fields": (
                    "longitude",
                    "latitude",
                )
            }
        )
    )
