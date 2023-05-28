from django.urls import path

from map.views import (
    PointListView,
    PointSearchView,
)

urlpatterns = [
    path("", PointListView.as_view(), name="points_list"),
    path("<str:query>", PointSearchView.as_view(), name="points_search"),
]
