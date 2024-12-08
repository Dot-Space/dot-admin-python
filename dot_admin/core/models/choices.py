from django.db import models


class DataTypeChoices(models.TextChoices):
    """
    Типы файлов.
    """

    IMAGE = 'image', 'Изображение'
    DOCUMENT = 'document', 'Документ'
    VIDEO = 'video', 'Видео'
    AUDIO = 'audio', 'Аудио'
