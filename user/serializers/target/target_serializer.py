from rest_framework import serializers

from user.models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = (
            "code",
            "name",
        )
        ref_name = "preference_result"
