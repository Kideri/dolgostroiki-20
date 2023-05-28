from rest_framework import serializers
from common.serializers import BaseResponseSerializer

from map.serializers import ListPointsSerializer


class ListPointsDocSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=ListPointsSerializer())
