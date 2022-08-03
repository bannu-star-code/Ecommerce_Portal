

from http.client import responses
from urllib import response


def auth_middleware(get_response):

    def middleware(request):

        respnse=get_response(request)

        return response
    return middleware