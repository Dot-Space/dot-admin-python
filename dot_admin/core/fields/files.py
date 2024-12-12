from rest_framework import serializers

from dot_admin.core.models.choices import DataTypeChoices


class DotFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    uri = serializers.URLField()
    is_main = serializers.BooleanField(default=False)
    data_type = serializers.ChoiceField(choices=DataTypeChoices.choices, allow_null=True)

    def get_uri(self, obj):
        request = self.context.get('request')
        try:
            file_url = obj.file.url
            return request.build_absolute_uri(file_url) if request else file_url
        except AttributeError:
            return None

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'uri': self.get_uri(instance),
            'is_main': instance.is_main,
            'data_type': instance.data_type,
        }


class DotFileListField(serializers.Field):

    def to_representation(self, value):
        request = self.context.get('request')
        if hasattr(value, 'all'):
            value = value.all()
        elif not isinstance(value, (list, tuple)):
            value = [value]
        serializer = DotFileSerializer(value, context={'request': request}, many=True)
        return serializer.data

    def to_internal_value(self, data):
        print(data)
        serializer = DotFileSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class DotFileField(serializers.Field):

    def to_representation(self, value):
        request = self.context.get('request')
        serializer = DotFileSerializer(value, context={'request': request})
        return serializer.data

    def to_internal_value(self, data):
        serializer = DotFileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
