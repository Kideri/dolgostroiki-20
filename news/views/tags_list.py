from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from news.docs import TagsListDocsSerializer
from news.models import Tag
from news.serializers import (
    TagsListSerializer
)


class TagsListView(BaseAPIView):
    response_serializer = TagsListSerializer

    @swagger_auto_schema(
        responses={200: TagsListDocsSerializer(), 401: BaseResponseSerializer()},
        tags=["News"],
        operation_id="Get tag list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in Tag.objects.all()]
