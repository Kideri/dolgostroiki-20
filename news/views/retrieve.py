from drf_yasg.utils import swagger_auto_schema

from common.execptions import CustomException
from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from news.docs import NewsRetrieveDocsSerializer
from news.models import News
from news.serializers import (
    NewsRetrieveSerializer
)


class NewsRetrieveView(BaseAPIView):
    response_serializer = NewsRetrieveSerializer
    news_id = None

    @swagger_auto_schema(
        responses={200: NewsRetrieveDocsSerializer(), 401: BaseResponseSerializer()},
        tags=["News"],
        operation_id="Get news",
    )
    def get(self, request, news_id: int = None):
        self.news_id = news_id
        return self.base_method()

    def get_result(self):
        object_ = News.objects.filter(id=self.news_id)
        if not object_.exists():
            raise CustomException("news not found")
        object_ = object_.first()
        return self.response_serializer(object_).data
