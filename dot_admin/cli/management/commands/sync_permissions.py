from django.core.management.base import BaseCommand
from django.apps import apps
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import importlib


class Command(BaseCommand):
    """
    Команда для синхронизации кастомных прав из permissions.py в базу данных
    """
    help = 'Синхронизирует кастомные права из permissions.py в базу данных'

    def handle(self, *args, **options):
        for app_config in apps.get_app_configs():
            try:
                permissions_module = importlib.import_module(f'{app_config.name}.permissions')
                permissions = getattr(permissions_module, 'PERMISSIONS', [])
                if permissions:
                    content_type, created = ContentType.objects.get_or_create(
                        app_label=app_config.label,
                        model='permission'
                    )
                    for perm in permissions:
                        codename = perm['codename']
                        name = perm['name']
                        permission, created = Permission.objects.get_or_create(
                            codename=codename,
                            content_type=content_type,
                            defaults={'name': name}
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Добавлено право: {codename}'))
                        else:
                            self.stdout.write(f'Право уже существует: {codename}')
            except ModuleNotFoundError:
                pass
