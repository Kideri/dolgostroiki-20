from rest_framework import serializers


class BaseResponseSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=255)
    result = serializers.JSONField(required=False)
    details = serializers.CharField(max_length=1024, required=False, help_text="Displays on status='error'")
