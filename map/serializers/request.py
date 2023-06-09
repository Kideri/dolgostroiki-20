from rest_framework import serializers
from map.models import Point


class CreatePointsSerializer(serializers.ModelSerializer):
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
