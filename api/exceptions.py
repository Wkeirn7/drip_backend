from rest_framework.exceptions import PermissionDenied
from rest_framework import status


class InvalidUserException(PermissionDenied):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "User information inconsistent"
    default_code = 'invalid'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code