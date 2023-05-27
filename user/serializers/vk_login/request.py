from rest_framework import serializers


class VkLoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    vk_access_token = serializers.CharField(max_length=2047, required=True)
