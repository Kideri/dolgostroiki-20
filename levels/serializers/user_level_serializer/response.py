from rest_framework import serializers
from levels.models import UserLevel, Config


class LevelConfigResponseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=2047, source='level_desc')

    class Meta:
        model = Config
        fields = (
            "id",
            "level",
            "exp",
            "description"
        )


class UserLevelResponseSerializer(serializers.ModelSerializer):
    current_level = LevelConfigResponseSerializer(source='get_current_level', required=False)

    class Meta:
        model = UserLevel
        fields = (
            "current_level",
            "total_exp",
        )
