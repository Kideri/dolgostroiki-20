from rest_framework import serializers
from map.models import Point


class ListPointsSerializer(serializers.ModelSerializer):
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
        )
