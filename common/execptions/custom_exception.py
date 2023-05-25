from rest_framework import status

from .base_exception import BaseAPIException


class CustomException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    details = "Something went wrong."
