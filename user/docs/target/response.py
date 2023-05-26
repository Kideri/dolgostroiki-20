from rest_framework import serializers
from common.serializers import BaseResponseSerializer
from user.serializers import TargetSerializer


class TargetesponseSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=TargetSerializer())

    class Meta:
        ref_name = "Target response"


class SetTargetResponseSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=serializers.CharField(max_length=31, help_text='Codes of set targets'))
