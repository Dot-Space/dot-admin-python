from inspect import trace

from django.db import models

from dot_admin.core.models.choices import DataTypeChoices


class BaseFile(models.Model):
    """
    Базовая модель файла.
    """

    name = models.CharField(
        'Название',
        max_length=255,
        null=True,
        blank=True,
    )

    file = models.FileField(
        'Файл',
    )

    is_main = models.BooleanField(
        'Основной',
        default=False,
    )

    data_type = models.CharField(
        'Тип',
        choices=DataTypeChoices.choices,
        max_length=8,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
