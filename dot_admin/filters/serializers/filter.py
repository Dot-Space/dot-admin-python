from typing import Type

from rest_framework import serializers

from dot_admin.filters.base_filter import BaseFilterField, BaseFilterValue


class BaseFilterValueSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для значений фильтра.
    """
    class Meta:
        model: Type[BaseFilterValue] = BaseFilterValue
        fields: tuple[str] = []


class BaseFilterFieldSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для фильтров.
    """
    values = serializers.SerializerMethodField()

    class Meta:
        model: Type[BaseFilterField] = BaseFilterField
        fields: tuple[str] = []

    def get_values(self, obj):
        ValueSerializer = self.context.get('value_serializer')
        if ValueSerializer:
            return ValueSerializer(obj.values.all(), many=True).data
        return []


def create_filter_value_serializer(serializer_model, *serializer_fields):
    """
    Создает класс сериализатора значений фильтра с переданными полями.
    """
    class GenericFilterValueSerializer(BaseFilterValueSerializer):
        class Meta(BaseFilterValueSerializer.Meta):
            model: Type[BaseFilterValue] = serializer_model
            fields: tuple[str] = serializer_fields

    return GenericFilterValueSerializer


def create_filter_field_serializer(filter_field_model, value_model, value_serializer_fields, *serializer_fields):
    """
    Создает класс сериализатора для фильтров с переданными полями.
    """
    ValueSerializer = create_filter_value_serializer(value_model, *value_serializer_fields)

    class GenericFilterFieldSerializer(BaseFilterFieldSerializer):
        class Meta(BaseFilterFieldSerializer.Meta):
            model = filter_field_model
            fields = serializer_fields

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.context['value_serializer'] = ValueSerializer

    return GenericFilterFieldSerializer