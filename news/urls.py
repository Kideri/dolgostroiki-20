from django.urls import path

from news.views import (
    NewsListView,
    NewsRetrieveView,
    TagsListView,
)

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
    path("<int:news_id>", NewsRetrieveView.as_view(), name="news_retrieve"),
    path("tags", TagsListView.as_view(), name="tags_list"),
]
