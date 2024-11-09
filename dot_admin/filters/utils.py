from typing import Dict, List, Type

from django.db.models import Model

from .serializers import create_filter_field_serializer


def get_filter_options(model: Type[Model], use_cache: bool) -> Dict[str, List[str]]:
    """
    Возвращает опции фильтров для модели

    :param use_cache: использовать ли кэш для хранения опций фильтров
    :param model: модель
    :return: словарь с опциями фильтров
    """
    filter_model = getattr(model, '_filter_field', None)
    if filter_model is None:
        return {}

    app_name = filter_model._meta.app_label
    model_name = filter_model._meta.model_name

    if use_cache:
        from django.core.cache import cache

        cached_filters = cache.get(f'{app_name}_{model_name}_filters')
        if cached_filters:
            return cached_filters

    filters = filter_model.objects.all()

    NaturalFilterFieldSerializer = create_filter_field_serializer(
        filter_model, filter_model.values.field.model, ('name',), 'name', 'type', 'values'
    )
    OriginalFilterFieldSerializer = create_filter_field_serializer(
        filter_model, filter_model.values.field.model, ('value',), 'code', 'type', 'values'
    )

    filter_options = NaturalFilterFieldSerializer(filters, many=True).data
    filter_options.extend(OriginalFilterFieldSerializer(filters, many=True).data)

    if use_cache:
        cache.set(f'{app_name}_{model_name}_filters', filter_options, timeout=60 * 60 * 24)

    return filter_options
