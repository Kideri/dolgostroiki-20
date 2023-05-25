from common.serializers import BaseResponseSerializer
from user.serializers import UserInfoSerializer


class UserInfoResponseSerializer(BaseResponseSerializer):
    result = UserInfoSerializer()

    class Meta:
        ref_name = "User response"
