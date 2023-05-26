from django.urls import path

from user.views import (
    LoginView,
    OtherUserInfoView,
    RegisterView,
    UpdateUserInfoView,
    UserInfoView,
    PreferencesListView,
    SetPreferencesView,
    TargetListView,
    SetTargetsView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("signin/", LoginView.as_view(), name="login"),
    path("me/", UserInfoView.as_view(), name="me"),
    path("user/<int:user_id>/", OtherUserInfoView.as_view(), name="user_info"),
    path("update_me/", UpdateUserInfoView.as_view(), name="update_user_info"),
    path("preferences/", PreferencesListView.as_view(), name="preferences_list"),
    path("set_preferences/", SetPreferencesView.as_view(), name="preferences_set"),
    path("target/", TargetListView.as_view(), name="targets_list"),
    path("set_targets/", SetTargetsView.as_view(), name="targets_set"),
]
