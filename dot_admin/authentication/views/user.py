from rest_framework import viewsets
from django.contrib.auth import get_user_model

from ..serializers import BaseUserSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления пользователями и их правами.
    """
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
