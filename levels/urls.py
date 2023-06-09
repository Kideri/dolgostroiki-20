from django.urls import path

from levels.views import (
    LevelsListView,
)

urlpatterns = [
    path("", LevelsListView.as_view(), name="levels_list"),
]
