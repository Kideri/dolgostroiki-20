from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from user.models import User, UserPreferences, UserTargets
from levels.models import UserLevel


class PreferenceInline(admin.TabularInline):
    model = UserPreferences


class TargetInline(admin.TabularInline):
    model = UserTargets


class LevelInline(admin.TabularInline):
    model = UserLevel

    readonly_fields = ["current_level", "total_exp"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        PreferenceInline,
        TargetInline,
        LevelInline
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
    readonly_fields = ("avatar_tag", "vk_id")
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
                    "vk_id",
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
