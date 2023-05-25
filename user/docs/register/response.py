from common.serializers import BaseResponseSerializer
from user.serializers import RegisterResult


class RegisterResponseSerializer(BaseResponseSerializer):
    result = RegisterResult()

    class Meta:
        ref_name = "Register response"
