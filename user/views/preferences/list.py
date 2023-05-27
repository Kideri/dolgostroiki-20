from typing import List

from drf_yasg.utils import swagger_auto_schema

import rest_framework.permissions
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import PreferenceResponseSerializer
from user.models import Preference
from user.serializers import (
    PreferenceSerializer
)


class PreferencesListView(BaseAPIView):
    response_serializer = PreferenceSerializer
    permission_classes: List[rest_framework.permissions.BasePermission] = [rest_framework.permissions.AllowAny]

    @swagger_auto_schema(
        responses={200: PreferenceResponseSerializer(), 401: BaseResponseSerializer()},
        tags=["Profile"],
        operation_id="Get preferences list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Preference.objects.all()]
