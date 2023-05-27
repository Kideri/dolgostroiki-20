from collections import OrderedDict

from rest_framework import serializers

from levels.serializers import UserLevelResponseSerializer
from user.models import User


class UpdateUserInfoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "avatar",
            "email",
            "age",
            "is_first_name_private",
            "is_age_private",
            "is_email_private",
            "is_date_joined_private",
            "is_vk_id_private",
        )
        ref_name = "user_info_update"


class UserInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=True)
    vk_id = serializers.IntegerField(read_only=True, required=False)
    role = serializers.CharField(max_length=255, read_only=True)
    avatar = serializers.ImageField(read_only=False)
    date_joined = serializers.DateTimeField(read_only=True)
    last_seen = serializers.DateTimeField(read_only=True)
    level = UserLevelResponseSerializer(source='user_current_level', required=False)
    preferences = serializers.ListField(
        child=serializers.CharField(max_length=255), required=False, help_text="User preferences codes",
        source="user_info_preferences", read_only=True
    )
    targets = serializers.ListField(
        child=serializers.CharField(max_length=255), required=False, help_text="User targets codes",
        source="user_info_targets", read_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "vk_id",
            "first_name",
            "avatar",
            "email",
            "date_joined",
            "last_seen",
            "role",
            "age",
            "level",
            "is_first_name_private",
            "is_age_private",
            "is_email_private",
            "is_date_joined_private",
            "preferences",
            "targets",
        )
        ref_name = "user_info_result"


class OtherUserInfoSerializer(serializers.ModelSerializer):
    vk_id = serializers.IntegerField(read_only=True, required=False, source="user_info_vk_id")
    first_name = serializers.CharField(max_length=255, source="user_info_first_name", required=False)
    age = serializers.IntegerField(source="user_info_age", required=False)
    avatar = serializers.ImageField(required=False)
    email = serializers.CharField(max_length=255, source="user_info_email", required=False)
    date_joined = serializers.CharField(max_length=255, source="user_info_date_joined", required=False)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = User
        fields = ("id", "vk_id", "avatar", "first_name", "age", "email", "username", "date_joined", "last_seen", "role")
        ref_name = "other_user_info_result"
