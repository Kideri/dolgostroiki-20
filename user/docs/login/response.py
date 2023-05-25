from rest_framework import serializers

from common.serializers import BaseResponseSerializer


class ResultSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=1024, required=True)


class ResponseSerializer(BaseResponseSerializer):
    result = ResultSerializer()
