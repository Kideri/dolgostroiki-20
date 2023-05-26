from rest_framework import serializers


class SetPreferencesRequestSerializer(serializers.Serializer):
    preferences = serializers.ListSerializer(child=serializers.CharField(max_length=31), required=True)
