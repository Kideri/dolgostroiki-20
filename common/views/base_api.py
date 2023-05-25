from abc import ABC, abstractmethod

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.execptions import BaseAPIException


class BaseAPIView(APIView, ABC):
    """
    Абстракция для создания всех АПИ
    При унаследовании необходимо переопределить требуемый метод АПИ, get_result()
    В требуемом методе необходимо вернуть результат выполнения base_method
    В случае успешного исполнения вернет статус-код 200 и ответ в формате:
        {"status": "ok", "result": self.get_result()}, status_code = HTTP 200
    В случае падения ошибки, унаследованной от BaseAPIException:
        {"status": "error", "details": BaseAPIException.details}, status_code = HTTP 400
    В случае падения любой не отловленной ошибки:
        {"status": "error", "details": str(Exception)}, status_code = HTTP 500
    Example:
        class SomeAPI(BaseAPIView):
            response_serializer = SomeClassResponseSerializer
            def post(self, request):
                return self.base_method()
            def result(self):
                *some code here to return ur object*
    """

    authentication_classes = [JWTAuthentication]
    request_serializer: serializers.Serializer = None
    response_serializer: serializers.Serializer = None

    def base_method(self) -> Response:
        try:
            result = self.get_result()
            return Response(data=self.get_result_response("ok", result=result))
        except BaseAPIException as e:
            return Response(data=self.get_result_response("error", error=e.details), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=self.get_result_response("error", error=str(e)), status=status.HTTP_200_OK)

    def get_result_response(self, status, result=None, error=None):
        response_data = {"status": status}
        if result:
            response_data["result"] = result
            return response_data
        if error:
            response_data["details"] = error
            return response_data

    def get_data_from_request(self):
        serializer = self.request_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return serializer

    @abstractmethod
    def get_result(self):
        raise NotImplementedError
