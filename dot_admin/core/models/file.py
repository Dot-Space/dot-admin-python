from django.db import models


class BaseFile(models.Model):
    """Базовая модель файла."""

    class Types(models.TextChoices):
        """Типы файлов."""
        IMAGE = 'image', 'Изображение'
        DOCUMENT = 'document', 'Документ'
        VIDEO = 'video', 'Видео'

    name = models.CharField(
        'Название',
        max_length=255,
    )
    file = models.FileField(
        'Файл',
    )
    is_main = models.BooleanField(
        'Основной',
        default=False,
    )
    type = models.CharField(
        'Тип',
        max_length=50,
    )


    class Meta:
        abstract = True
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'