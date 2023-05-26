from drf_yasg.utils import swagger_auto_schema

from common.serializers import BaseResponseSerializer
from common.views.base_api import BaseAPIView
from user.docs import SetTargetResponseSerializer
from user.models import Target, UserTargets
from user.serializers import (
    SetTargetsRequestSerializer
)


class SetTargetsView(BaseAPIView):
    request_serializer = SetTargetsRequestSerializer
    response_serializer = None

    @swagger_auto_schema(
        responses={200: SetTargetResponseSerializer(), 401: BaseResponseSerializer()},
        request_body=SetTargetsRequestSerializer(),
        tags=["Profile"],
        operation_id="Set targets",
    )
    def put(self, request):
        return self.base_method()

    def get_result(self):
        targets_to_set = self.get_data_from_request().data.get('targets')
        targets = Target.objects.filter(code__in=targets_to_set).all()

        self.request.user.targets.all().delete()
        for target in targets:
            UserTargets.objects.create(user=self.request.user, target=target)

        return self.request.user.user_info_targets
