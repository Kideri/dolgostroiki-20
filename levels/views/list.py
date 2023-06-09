from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from levels.docs import LevelConfigDocsResponseSerializer
from levels.models import Config
from levels.serializers import (
    LevelConfigResponseSerializer
)


class LevelsListView(BaseAPIView):
    response_serializer = LevelConfigResponseSerializer

    @swagger_auto_schema(
        responses={200: LevelConfigDocsResponseSerializer(), 401: BaseResponseSerializer()},
        tags=["Map"],
        operation_id="Get levels list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Config.objects.all()]
