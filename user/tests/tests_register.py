from django.urls import reverse_lazy

from common.tests import BaseGameTestCase


class RegisterTestCase(BaseGameTestCase):
    url = reverse_lazy("register")

    def setUp(self):
        super().setUp()
        self._user_data = {
            "password": "testuserpassword123",
            "password2": "testuserpassword123",
            "email": "sometestemail@mail.com",
            "first_name": "sometestfirstname",
            "age": 25,
        }

    def test__register_new_account__ok(self):
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "result" in response_data
        assert "access" in response_data["result"]

    def test__register_new_account_with_already_exists_account_fails__ok(self):
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "result" in response_data
        assert "access" in response_data["result"]
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data

    def test__register_new_account_with_not_valid_email__ok(self):
        self._user_data["email"] = "notvalid"
        response = self._client_post(self._user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "details" in response_data

    # def test__register_new_account_with_not_valid_pass__ok(self):
    #     self._user_data["password"] = "inv"  # noqa: S105
    #     self._user_data["password2"] = "inv"
    #     response = self._client_post(self._user_data)
    #     assert response.status_code == 200
    #     response_data = response.json()
    #     assert "details" in response_data

    # def test__register_new_account_without_some_data__ok(self):
    #     self._user_data.pop("first_name")
    #     response = self._client_post(self._user_data)
    #     assert response.status_code == 200
    #     response_data = response.json()
    #     assert "details" in response_data
