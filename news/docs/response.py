from common.serializers import BaseResponseSerializer

from news.serializers import NewsListSerializer, NewsRetrieveSerializer, TagsListSerializer


class NewsListDocsSerializer(BaseResponseSerializer):
    result = NewsListSerializer()


class NewsRetrieveDocsSerializer(BaseResponseSerializer):
    result = NewsRetrieveSerializer()


class TagsListDocsSerializer(BaseResponseSerializer):
    result = TagsListSerializer()
