from rest_framework import serializers
from common.serializers import BaseResponseSerializer
from levels.serializers import LevelConfigResponseSerializer


class LevelConfigDocsResponseSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=LevelConfigResponseSerializer)
