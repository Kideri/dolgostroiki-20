from rest_framework import serializers

from news.models import News, Tag


class NewsListSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=256, help_text='Shorten version of text', source='shorten_text')
    tags = serializers.ListSerializer(child=serializers.IntegerField(), source='tags_serialize')

    class Meta:
        model = News
        fields = (
            "id",
            "image",
            "title",
            "text",
            "tags",
        )
        ref_name = "news_list_result"


class NewsRetrieveSerializer(serializers.ModelSerializer):
    tags = serializers.ListSerializer(child=serializers.IntegerField(), source='tags_serialize')

    class Meta:
        model = News
        fields = (
            "image",
            "title",
            "text",
            "tags",
        )
        ref_name = "news_retrieve_result"


class TagsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "title",
            "background_color",
        )
        ref_name = "tags_list_result"
