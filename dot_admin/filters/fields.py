from django.db import models


class BaseFilterSet(models.Model):
    """
    Абстрактная модель "Набор фильтров"

    Эта модель представляет набор фильтров с названием и названием модели, к которой он применяется.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    model_name = models.CharField(verbose_name='Модель', max_length=255)

    class Meta:
        abstract = True


class BaseFilterField(models.Model):
    """
    Абстрактная модель "Фильтр"

    Эта модель представляет фильтр с названием и кодовым названием.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Код', max_length=255)
    is_many = models.BooleanField(verbose_name='Множественный выбор', default=False)
    type = models.CharField(verbose_name='Тип', max_length=255, default='string')
    filter_set = models.ForeignKey(BaseFilterSet, null=True, blank=True, verbose_name='Набор фильтров',
                                   related_name='fields', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BaseFilterValue(models.Model):
    """
    Абстрактная модель "Значение фильтра"

    Эта модель представляет значение фильтра с названием и значением.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    value = models.CharField(verbose_name='Значение', max_length=255)
    filter_class = models.ForeignKey(BaseFilterField, verbose_name='Фильтр', related_name='values', on_delete=models.CASCADE)

    class Meta:
        abstract = True
