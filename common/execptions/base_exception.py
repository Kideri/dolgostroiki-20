from rest_framework import status


class BaseAPIException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    details = "Something went wrong"

    def __init__(
        self,
        details: str = None,
    ):
        self.details = details or self.details

    def __str__(self):
        details = f": {self.details}" if self.details else ""
        return f"{details}"
