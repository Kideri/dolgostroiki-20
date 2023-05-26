from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import UserInfoResponseSerializer
from user.serializers import UpdateUserInfoSerializer


class UpdateUserInfoView(BaseAPIView):
    response_serializer = UpdateUserInfoSerializer
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        responses={200: UserInfoResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=UpdateUserInfoSerializer(),
        tags=["Profile"],
        operation_id="Update self user info",
    )
    def post(self, request):
        return self.base_method()

    def get_result(self):
        user = self.request.user
        serializer = UpdateUserInfoSerializer(instance=user, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return self.response_serializer(user).data
