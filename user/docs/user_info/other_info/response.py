from rest_framework import serializers

from common.serializers import BaseResponseSerializer
from user.models import UserRole


class OtherUserInfoSchemaSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    vk_id = serializers.IntegerField(required=False)
    avatar = serializers.ImageField(required=False)
    first_name = serializers.CharField(max_length=255, required=False)
    age = serializers.IntegerField(min_value=12, max_value=99, required=False)
    email = serializers.CharField(max_length=255, required=False)
    date_joined = serializers.CharField(max_length=255, required=False)
    last_seen = serializers.DateTimeField(required=True)
    role = serializers.ChoiceField(choices=UserRole.choices, required=True)


class OtherUserInfoResponseSerializer(BaseResponseSerializer):
    result = OtherUserInfoSchemaSerializer()

    class Meta:
        ref_name = "Other user response"
