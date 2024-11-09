import jwt
from django.conf import settings


def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token
