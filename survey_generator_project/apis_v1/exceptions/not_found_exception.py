from rest_framework import status
from rest_framework.exceptions import APIException


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = '404'

    def __init__(self, message):
        super().__init__(message)