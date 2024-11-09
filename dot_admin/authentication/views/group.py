from rest_framework import viewsets
from django.contrib.auth.models import Group
from ..serializers import BaseGroupSerializer
from ..permissions import IsAdminUserOrHasPermission, IsAuthenticated


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = BaseGroupSerializer

    def get_permissions(self):
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
