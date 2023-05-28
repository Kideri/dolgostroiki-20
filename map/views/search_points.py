from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from map.docs import ListPointsDocSerializer
from map.models import Point
from map.serializers import (
    ListPointsSerializer
)


class PointSearchView(BaseAPIView):
    response_serializer = ListPointsSerializer
    query: str = None

    @swagger_auto_schema(
        responses={200: ListPointsDocSerializer(), 401: BaseResponseSerializer()},
        tags=["Map"],
        operation_id="Search points by name",
    )
    def get(self, request, query: str = None):
        self.query = query
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Point.objects.filter(name__icontains=self.query).all()]
