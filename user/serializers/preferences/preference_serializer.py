from rest_framework import serializers

from user.models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = (
            "code",
            "name",
        )
        ref_name = "preference_result"
