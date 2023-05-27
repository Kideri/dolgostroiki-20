from typing import List

import rest_framework.permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from common.serializers import BaseResponseSerializer
from common.views import BaseAPIView
from user.docs import LoginRequest, LoginResponseSerializer, LoginResult


class LoginView(BaseAPIView):
    request_serializer = TokenObtainPairSerializer
    response_serializer = LoginResult
    permission_classes: List[rest_framework.permissions.BasePermission] = [rest_framework.permissions.AllowAny]

    @swagger_auto_schema(
        responses={200: LoginResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=LoginRequest(),
        tags=["Auth"],
        operation_id="SignIn user",
    )
    def post(self, request):
        return self.base_method()

    def get_result(self):
        serializer = self.request_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return {'access': serializer.validated_data['access']}
