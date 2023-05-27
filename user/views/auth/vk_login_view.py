from typing import List

import requests
from drf_yasg.utils import swagger_auto_schema
import rest_framework.permissions

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.models import User
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
        request_data = self.get_data_from_request().data
        vk_access_token = request_data.get('vk_access_token')
        email = request_data.get('email')

        url = f'https://api.vk.com/method/account.getProfileInfo?access_token={vk_access_token}&v=5.131'

        data = requests.post(url).json()
        if 'error' in data:
            raise CustomException('invalid_token')

        data = data.get('response')
        vk_id = data.get('id')

        user = User.objects.filter(vk_id=vk_id).first()

        if user:
            return {"access": user.access_token}

        user = User.objects.create(email=email, vk_id=vk_id, first_name=data.get('first_name'))
        user.save()

        return {"access": user.access_token}
