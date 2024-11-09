from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings


User = get_user_model()

class JWTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token=None):
        if token is None:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return user
        except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
