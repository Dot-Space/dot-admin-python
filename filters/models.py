from django.db import models

class FilterField(models.Model):
    """
    Абстрактная модель "Фильтр"

    Эта модель представляет фильтр с названием и кодовым названием.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Код', max_length=255)

    class Meta:
        abstract = True

class FilterValue(models.Model):
    """
    Абстрактная модель "Значение фильтра"

    Эта модель представляет значение фильтра с названием и значением.
    """
    name = models.CharField(verbose_name='Название', max_length=255)
    value = models.CharField(verbose_name='Значение', max_length=255)
    filter_class = models.ForeignKey(FilterField, verbose_name='Фильтр', related_name='values', on_delete=models.CASCADE)

    class Meta:
        abstract = True
        