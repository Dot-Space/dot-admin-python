from functools import wraps
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


def permission_required(perms):
    def decorator(func):
        @wraps(func)
        def wrapped(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise NotAuthenticated('Необходима авторизация')
            for perm in perms:
                if not request.user.has_perm(perm):
                    raise PermissionDenied(f'У вас нет разрешения: {perm}')
            return func(self, request, *args, **kwargs)
        return wrapped
    return decorator
