from rest_framework import serializers

from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1024, help_text='Shorten version of text')

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
        )
        ref_name = "news_list_result"


class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "text",
        )
        ref_name = "news_retrieve_result"
