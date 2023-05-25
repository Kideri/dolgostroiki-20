from typing import List

import rest_framework.permissions
from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views import BaseAPIView
from user.docs import RegisterResponseSerializer
from user.serializers import RegisterRequest, RegisterResult


class RegisterView(BaseAPIView):
    request_serializer = RegisterRequest
    response_serializer = RegisterResult
    permission_classes: List[rest_framework.permissions.BasePermission] = []

    @swagger_auto_schema(
        responses={200: RegisterResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=RegisterRequest(),
        tags=["Auth"],
        operation_id="SignUp player",
    )
    def post(self, request):
        return self.base_method()

    def get_result(self):
        serializer = self.request_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return self.response_serializer(user).data
