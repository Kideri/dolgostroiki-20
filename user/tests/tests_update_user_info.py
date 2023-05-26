from django.urls import reverse_lazy

from common.tests import BaseGameCoreTestCase


class TestSelfUserInfo(BaseGameCoreTestCase):
    url = reverse_lazy("update_user_info")

    def setUp(self) -> None:
        super().setUp()
        self.data = {
            "first_name": "Test user",
            "age": 35,
            "is_first_name_private": True,
            "is_age_private": False,
        }

    def test__get_self_user_info__ok(self):
        response = self._client_post(self.data)
        assert response.status_code == 200
        assert "result" in response.json()
        response_data = response.json()["result"]
        assert "date_joined" in response_data
        assert "last_seen" in response_data
        expected = {
            "id": self.user.id,
            "first_name": "Test user",
            "avatar": None,
            "age": 35,
            "email": "test@email.ru",
            "role": "D",
            "date_joined": response_data["date_joined"],
            "last_seen": response_data["last_seen"],
            "is_first_name_private": True,
            "is_age_private": False,
            "is_email_private": True,
            "is_date_joined_private": True,
            "preferences": [],
            "targets": [],
        }
        self.user.refresh_from_db()
        assert response_data == expected
        assert response_data["date_joined"] != ""
        assert response_data["last_seen"] != ""
        assert self.user.first_name == "Test user"
        assert self.user.age == 35
        assert self.user.is_first_name_private
        assert not self.user.is_age_private
