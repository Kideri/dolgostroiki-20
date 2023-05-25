from rest_framework import serializers

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    access = serializers.CharField(max_length=1024, required=True, source="access_token")

    class Meta:
        model = User
        fields = ("access",)
        ref_name = "register_result"
