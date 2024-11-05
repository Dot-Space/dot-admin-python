from typing import Type

from rest_framework import viewsets

from dot_admin.filters.base_filter import BaseFilterField
from dot_admin.filters.serializers.filter import FilterFieldSerializer


class BaseFilterViewSet(viewsets.ModelViewSet):
    """
    Базовый ViewSet для управления фильтрами
    """

    queryset: Type[BaseFilterField]
    serializer_class: Type[FilterFieldSerializer]