from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from user.models import User, UserPreferences, UserTargets


class PreferenceInline(admin.TabularInline):
    model = UserPreferences


class TargetInline(admin.TabularInline):
    model = UserTargets


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        PreferenceInline,
        TargetInline
    ]
    list_display = (
        "id",
        "role",
        "is_active",
        "is_staff",
    )
    list_display_links = ("id", )
    search_fields = ("first_name", "age", "email", "id")
    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )
    date_hierarchy = "date_joined"
    readonly_fields = ("avatar_tag", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "role",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "avatar_tag",
                    "avatar",
                    "first_name",
                    "email",
                    "age",
                )
            },
        ),
        (
            _("Account information availability"),
            {
                "fields": (
                    "is_first_name_private",
                    "is_age_private",
                    "is_email_private",
                    "is_date_joined_private",
                )
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "last_seen", "date_joined")},
        ),
    )
