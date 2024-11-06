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


def create_filter_value_serializer(value_model, *value_serializer_fields):
    """
    Создает класс сериализатора полей фильтра.
    """
    class GenericFilterValueSerializer(BaseFilterValueSerializer):
        class Meta:
            model: Type[BaseFilterValue] = value_model
            fields: tuple[str] = value_serializer_fields

    return GenericFilterValueSerializer

def create_filter_field_serializer(filter_field_model, value_model, value_serializer_fields, *serializer_fields):
    """
    Создает класс сериализатора значений фильтра с переданными полями.
    """
    class GenericFilterValueSerializer(BaseFilterValueSerializer):
        class Meta:
            model: Type[BaseFilterValue] = value_model
            fields: tuple[str] = value_serializer_fields

    class GenericFilterFieldSerializer(BaseFilterFieldSerializer):
        values = GenericFilterValueSerializer(many=True, read_only=True)

        class Meta:
            model: Type[BaseFilterField] = filter_field_model
            fields: tuple[str] = serializer_fields

    return GenericFilterFieldSerializer
