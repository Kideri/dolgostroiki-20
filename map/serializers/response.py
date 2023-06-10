from rest_framework import serializers
from map.models import Point


class ListPointsSerializer(serializers.ModelSerializer):
    preferences = serializers.ListSerializer(child=serializers.CharField(max_length=31), source="preferences_serialize")

    class Meta:
        model = Point
        fields = (
            "longitude",
            "latitude",
            "name",
            "description",
            "work_time",
            "address",
            "phone_number",
            "preferences",
        )
