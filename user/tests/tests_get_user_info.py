from django.urls import reverse_lazy

from common.tests import BaseGameCoreTestCase
from user.models import User


class TestSelfUserInfo(BaseGameCoreTestCase):
    url = reverse_lazy("me")

    def setUp(self) -> None:
        super().setUp()

    def test__get_self_user_info__ok(self):
        response = self._client_get()
        assert response.status_code == 200
        assert "result" in response.json()
        response_data = response.json()["result"]
        assert "date_joined" in response_data
        assert "last_seen" in response_data
        expected = {
            "id": self.user.id,
            "first_name": None,
            "age": 18,
            "email": "test@email.ru",
            "role": "D",
            "date_joined": response_data["date_joined"],
            "last_seen": response_data["last_seen"],
            "is_first_name_private": False,
            "is_age_private": True,
            "is_email_private": True,
            "is_date_joined_private": True,
            "targets": [],
            "preferences": [],
        }
        assert response_data == expected
        assert response_data["date_joined"] != ""
        assert response_data["last_seen"] != ""


class TestOtherUserInfo(BaseGameCoreTestCase):
    url = reverse_lazy("user_info", kwargs={"user_id": 2})

    def setUp(self) -> None:
        super().setUp()
        self.other_user = User.objects.create(id=2, email="test2@email.ru", age=22)

    def test__get_other_user_info__ok(self):
        self.url = reverse_lazy("user_info", kwargs={"user_id": self.other_user.id})
        response = self._client_get()
        assert response.status_code == 200
        assert "result" in response.json()
        response_data = response.json()["result"]
        assert "last_seen" in response_data
        expected = {
            "id": self.other_user.id,
            "first_name": None,
            "last_seen": response_data["last_seen"],
            "role": "D"
        }
        assert response_data == expected, response_data
        assert response_data["last_seen"] != ""

    def test__get_other_user_info_with_update_privacy__ok(self):
        self.other_user.is_first_name_private = True
        self.other_user.is_age_private = False
        self.other_user.is_email_private = False
        self.other_user.is_date_joined_private = False
        self.other_user.save()
        self.url = reverse_lazy("user_info", kwargs={"user_id": self.other_user.id})
        response = self._client_get()
        assert response.status_code == 200
        assert "result" in response.json()
        response_data = response.json()["result"]
        assert "date_joined" in response_data
        assert "last_seen" in response_data
        expected = {
            "id": self.other_user.id,
            "age": 22,
            "email": "test2@email.ru",
            "date_joined": response_data["date_joined"],
            "last_seen": response_data["last_seen"],
            "role": "D"
        }
        assert response_data == expected, response_data
        assert response_data["date_joined"] != ""
        assert response_data["last_seen"] != ""

    def test__get_other_user_info_user_not_exists__ok(self):
        self.url = reverse_lazy("user_info", kwargs={"user_id": 101204029})
        response = self._client_get()
        assert response.status_code == 200
        assert "details" in response.json()
        assert response.json()["status"] == "error"
        assert response.json()["details"] == "user not found"
