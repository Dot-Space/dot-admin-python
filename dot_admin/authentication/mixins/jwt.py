from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
from ..backends import JWTAuthenticationBackend


class JWTAuthenticationMixin:
    def authenticate_request(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b'bearer':
            raise exceptions.AuthenticationFailed('No token provided')
        token = auth_header[1]
        backend = JWTAuthenticationBackend()
        user = backend.authenticate(request, token=token)
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid token')
        request.user = user
        return user
