from typing import List

import requests
from drf_yasg.utils import swagger_auto_schema
import rest_framework.permissions

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import LoginResponseSerializer
from user.serializers import (
    VkLoginRequestSerializer
)


class VkLoginView(BaseAPIView):
    request_serializer = VkLoginRequestSerializer
    response_serializer = None
    permission_classes: List[rest_framework.permissions.BasePermission] = []

    @swagger_auto_schema(
        responses={200: LoginResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=VkLoginRequestSerializer(),
        tags=["Auth"],
        operation_id="Login via VK",
    )
    def post(self, request):
        return self.base_method()

    def get_result(self):
        vk_access_token = self.get_data_from_request().data.get('vk_access_token')

        url = f'https://api.vk.com/method/account.getProfileInfo?access_token={vk_access_token}'

        print(vk_access_token)
        print(requests.post(url).json())

        return "abracadabra_upcoming"
