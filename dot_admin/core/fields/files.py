from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    uri = serializers.URLField()
    is_main = serializers.BooleanField()
    type = serializers.CharField(max_length=50)


class FileListSerializer(serializers.ListSerializer):
    child = FileSerializer()


class FileListField(serializers.Field):
    def to_representation(self, value):
        serializer = FileListSerializer(value, many=True)
        return serializer.data

    def to_internal_value(self, data):
        serializer = FileListSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class FileField(serializers.Field):
    def to_representation(self, value):
        serializer = FileSerializer(value)
        return serializer.data

    def to_internal_value(self, data):
        serializer = FileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data