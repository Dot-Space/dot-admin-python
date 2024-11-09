from rest_framework.permissions import BasePermission, IsAdminUser


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsAdminUserOrHasPermission(BasePermission):
    """
    Разрешение, которое позволяет доступ администраторам или пользователям с определенным правом.
    """

    def __init__(self, permission_codename=None):
        self.permission_codename = permission_codename

    def has_permission(self, request, view):
        if IsAdminUser().has_permission(request, view):
            return True
        if self.permission_codename:
            return request.user.has_perm(self.permission_codename)
        return False
