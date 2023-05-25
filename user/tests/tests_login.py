from django.urls import reverse_lazy

from common.tests import BaseGameTestCase
from user.models import User


class LoginTestCase(BaseGameTestCase):
    url = reverse_lazy("login")

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(email="test3@email.ru", age=75)
        self.user.set_password("test_u_password")
        self.user.save()
        self._user_data = {
            "email": "test3@email.ru",
            "password": "test_u_password",
        }

    def test__login__ok(self):
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "result" in response_data
        assert "access" in response_data["result"]

    def test__login_with_not_valid_data_fails__ok(self):
        self._user_data["email"] = "fail@email.ru"
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data
        self._user_data["email"] = "test3@email.ru"
        self._user_data["password"] = "fail"  # noqa: S105
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data

    def test__login_without_some_data_fails__ok(self):
        self._user_data.pop("email")
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data
        self._user_data["email"] = "test3@email.ru"
        self._user_data.pop("password")
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data
