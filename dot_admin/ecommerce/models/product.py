from django.db import models

from dot_admin.filters.fields import BaseFilterField
from dot_admin.filters.base.model import FilterableModel


class BaseProduct(FilterableModel):
    """
    Абстрактная модель "Товар"

    Эта модель представляет товар с названием, ценой, популярностью и флагом публикации.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    price = models.IntegerField(verbose_name='Цена')
    popularity = models.IntegerField(verbose_name='Популярность', default=0)
    is_published = models.BooleanField(verbose_name='Опубликован', default=False)

    FilterField = BaseFilterField

    class Meta:
        abstract = True

    def __str__(self):
        return self.name