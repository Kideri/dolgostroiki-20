from rest_framework import serializers
from common.serializers import BaseResponseSerializer
from user.serializers import PreferenceSerializer


class PreferenceResponseSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=PreferenceSerializer())

    class Meta:
        ref_name = "Preference response"


class SetPreferenceResponseSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=serializers.CharField(max_length=31, help_text='Codes of set preferences'))
