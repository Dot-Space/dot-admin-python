from django.db import models

from dot_admin.filters.base_filter import BaseFilterValue, BaseFilterField
from dot_admin.filters.filterable.manager import FilterableManager
from dot_admin.filters.filterable.meta import FilterableMeta


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
