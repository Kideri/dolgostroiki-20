import json

from django.test import TestCase
from rest_framework.test import APIClient


class BaseGameTestCase(TestCase):
    @property
    def url(self) -> str:
        raise NotImplementedError

    def setUp(self) -> None:
        self.client = APIClient()
        self.maxDiff = None

    def _client_post(self, json_data):
        return self.client.post(self.url, data=json.dumps(json_data), content_type="application/json")

    def _client_get(self):
        return self.client.get(self.url, content_type="application/json")
