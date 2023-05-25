from common.serializers import BaseResponseSerializer

from news.serializers import NewsListSerializer, NewsRetrieveSerializer


class NewsListDocsSerializer(BaseResponseSerializer):
    result = NewsListSerializer()


class NewsRetrieveDocsSerializer(BaseResponseSerializer):
    result = NewsRetrieveSerializer()
