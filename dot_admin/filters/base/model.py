from django.db import models

from ..fields import BaseFilterValue, BaseFilterField
from .manager import FilterableManager
from .meta import FilterableMeta


class FilterableModel(models.Model, metaclass=FilterableMeta):
    """
    Абстрактная модель "Фильтруемая модель"

    Эта модель представляет модель с фильтрами.
    """
    filters = models.ManyToManyField(BaseFilterValue, related_name='products')
    objects = FilterableManager

    FilterField = BaseFilterField

    class Meta:
        abstract = True
