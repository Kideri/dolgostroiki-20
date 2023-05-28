from rest_framework import serializers
from common.serializers import BaseResponseSerializer

from news.serializers import NewsListSerializer, NewsRetrieveSerializer, TagsListSerializer


class NewsListDocsSerializer(BaseResponseSerializer):
    result = serializers.ListSerializer(child=NewsListSerializer())


class NewsRetrieveDocsSerializer(BaseResponseSerializer):
    result = NewsRetrieveSerializer()


class TagsListDocsSerializer(BaseResponseSerializer):
    result = TagsListSerializer()
