from rest_framework import serializers


class VkLoginRequestSerializer(serializers.Serializer):
    vk_access_token = serializers.CharField(max_length=2047)
