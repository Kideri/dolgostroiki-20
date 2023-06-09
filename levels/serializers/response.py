from rest_framework import serializers
from levels.models import Config


class LevelConfigResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = (
            "level",
            "exp",
        )
