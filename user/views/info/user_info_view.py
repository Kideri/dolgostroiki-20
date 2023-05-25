from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import OtherUserInfoResponseSerializer, UserInfoResponseSerializer
from user.models import User
from user.serializers import (
    OtherUserInfoSerializer,
    UserInfoSerializer,
)


class UserInfoView(BaseAPIView):
    response_serializer = UserInfoSerializer

    @swagger_auto_schema(
        responses={200: UserInfoResponseSerializer(), 401: BaseResponseSerializer()},
        tags=["Profile"],
        operation_id="Get self user info",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return self.response_serializer(self.request.user).data


class OtherUserInfoView(BaseAPIView):
    response_serializer = OtherUserInfoSerializer

    @swagger_auto_schema(
        responses={200: OtherUserInfoResponseSerializer(), 401: BaseResponseSerializer()},
        tags=["Profile"],
        operation_id="Get other user info",
    )
    def get(self, request, *args, **kwargs):
        return self.base_method()

    def get_result(self):
        user_id = self.request.parser_context["kwargs"]["user_id"]
        for_user = User.objects.filter(id=user_id)
        if not for_user.exists():
            raise CustomException("user not found")
        for_user = for_user.first()
        return self.response_serializer(for_user).data
