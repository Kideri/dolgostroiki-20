from django.urls import path

from map.views import (
    PointListView,
    PointSearchView,
    CreatePointView,
)

urlpatterns = [
    path("", PointListView.as_view(), name="points_list"),
    path("create", CreatePointView.as_view(), name="create_point"),
    path("<str:query>", PointSearchView.as_view(), name="points_search"),
]
