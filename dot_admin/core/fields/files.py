from rest_framework import serializers

from dot_admin.core.models.choices import DataTypeChoices


class DotFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    uri = serializers.URLField()
    is_main = serializers.BooleanField(default=False)
    data_type = serializers.CharField(max_length=8, allow_null=True)
    data_type = serializers.ChoiceField(choices=DataTypeChoices.choices, allow_null=True)


class DotFileListSerializer(serializers.ListSerializer):
    child = DotFileSerializer()


class DotFileListField(serializers.Field):
    def to_representation(self, value):
        serializer = DotFileListSerializer(value, many=True)
        return serializer.data

    def to_internal_value(self, data):
        serializer = DotFileListSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class DotFileField(serializers.Field):
    def to_representation(self, value):
        serializer = DotFileSerializer(value)
        return serializer.data

    def to_internal_value(self, data):
        serializer = DotFileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
