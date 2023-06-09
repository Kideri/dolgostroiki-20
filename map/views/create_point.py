from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from map.serializers import CreatePointsSerializer


class CreatePointView(BaseAPIView):
    response_serializer = CreatePointsSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        responses={200: None, 401: BaseResponseSerializer()},
        request_body=CreatePointsSerializer(),
        tags=["Map"],
        operation_id="Create point",
    )
    def post(self, request):
        return self.base_method()

    def get_result(self):
        serializer = CreatePointsSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return None
