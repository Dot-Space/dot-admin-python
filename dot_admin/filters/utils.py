from typing import Dict, List, Type

from django.db.models import Model
from django.core.cache import cache

from .serializers.filter import FilterFieldSerializer, OriginalFilterFieldSerializer


def get_filter_options(model: Type[Model]) -> Dict[str, List[str]]:
    """
    Возвращает опции фильтров для модели

    :param model: модель
    :return: словарь с опциями фильтров
    """
    filter_model = getattr(model, '_filter_field', None)
    if filter_model is None:
        return {}

    app_name = filter_model._meta.app_label
    model_name = filter_model._meta.model_name

    cached_filters = cache.get(f'{app_name}_{model_name}_filters')
    if cached_filters:
        return cached_filters

    filters = filter_model.objects.all()
    filter_options = FilterFieldSerializer(filters, many=True).data
    filter_options.extend(OriginalFilterFieldSerializer(filters, many=True).data)

    cache.set(f'{app_name}_{model_name}_filters', filter_options, timeout=60 * 60 * 24)

    return filter_options
