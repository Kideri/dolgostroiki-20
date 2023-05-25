from abc import ABC

from common.tests import BaseGameTestCase
from user.models import User


class BaseGameCoreTestCase(BaseGameTestCase, ABC):
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(id=1, email="test@email.ru", age=18)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user.access_token}")
