from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import TargetesponseSerializer
from user.models import Target
from user.serializers import (
    TargetSerializer
)


class TargetListView(BaseAPIView):
    response_serializer = TargetSerializer

    @swagger_auto_schema(
        responses={200: TargetesponseSerializer(), 401: BaseResponseSerializer()},
        tags=["Target"],
        operation_id="Get targets list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Target.objects.all()]
