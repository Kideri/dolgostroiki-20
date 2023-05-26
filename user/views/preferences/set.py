from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import SetPreferenceResponseSerializer
from user.models import Preference, UserPreferences
from user.serializers import (
    SetPreferencesRequestSerializer
)


class SetPreferencesView(BaseAPIView):
    request_serializer = SetPreferencesRequestSerializer
    response_serializer = None

    @swagger_auto_schema(
        responses={200: SetPreferenceResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=SetPreferencesRequestSerializer(),
        tags=["Profile"],
        operation_id="Set preferences",
    )
    def put(self, request):
        return self.base_method()

    def get_result(self):
        preferences_to_set = self.get_data_from_request().data.get('preferences')
        preferences = Preference.objects.filter(code__in=preferences_to_set).all()

        self.request.user.preferences.all().delete()
        for preference in preferences:
            UserPreferences.objects.create(user=self.request.user, preference=preference)

        return self.request.user.user_info_preferences
