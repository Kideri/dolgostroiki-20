from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from news.docs import NewsListDocsSerializer
from news.models import News
from news.serializers import (
    NewsListSerializer
)


class NewsListView(BaseAPIView):
    response_serializer = NewsListSerializer

    @swagger_auto_schema(
        responses={200: NewsListDocsSerializer(), 401: BaseResponseSerializer()},
        tags=["News"],
        operation_id="Get news list",
    )
    def get(self, request):
        return self.base_method()

    def get_result(self):
        return [self.response_serializer(_).data for _ in News.objects.all()]
