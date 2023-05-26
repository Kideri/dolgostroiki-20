from rest_framework import serializers


class SetTargetsRequestSerializer(serializers.Serializer):
    targets = serializers.ListSerializer(child=serializers.CharField(max_length=31), required=True)
