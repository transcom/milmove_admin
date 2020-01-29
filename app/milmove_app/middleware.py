# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djangooidc.exceptions import OIDCException


class OIDCExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, OIDCException):
            return HttpResponse(str(exception), status=exception.status_code)
