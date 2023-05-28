from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from map.docs import ListPointsDocSerializer
from map.models import Point
from map.serializers import (
    ListPointsSerializer
)


class PointListView(BaseAPIView):
    response_serializer = ListPointsSerializer

    @swagger_auto_schema(
        responses={200: ListPointsDocSerializer(), 401: BaseResponseSerializer()},
        tags=["Map"],
        operation_id="Get points list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Point.objects.all()]
