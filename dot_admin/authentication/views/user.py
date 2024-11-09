from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from ..serializers import BaseUserSerializer, BaseGroupSerializer, BasePermissionSerializer
from ..permissions import IsAdminUserOrHasPermission


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления пользователями и их правами.
    """
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrHasPermission]

    def get_permissions(self):
        """
        Назначаем разрешения в зависимости от действия.
        """
        if self.action in ['list', 'retrieve']:
            permission = 'auth.user'
        elif self.action == 'create':
            permission = 'auth.user'
        elif self.action in ['update', 'partial_update']:
            permission = 'auth.user'
        elif self.action == 'destroy':
            permission = 'auth.user'
        else:
            permission = None

        if permission:
            self.permission_classes = [IsAuthenticated, IsAdminUserOrHasPermission(permission)]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
