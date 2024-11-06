from typing import Type

from rest_framework import viewsets

from dot_admin.filters.base_filter import BaseFilterField
from dot_admin.filters.serializers.filter import BaseFilterFieldSerializer


class BaseFilterViewSet(viewsets.ModelViewSet):
    """
    Базовый ViewSet для управления фильтрами
    """

    queryset: Type[BaseFilterField]
    serializer_class: Type[BaseFilterFieldSerializer]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
