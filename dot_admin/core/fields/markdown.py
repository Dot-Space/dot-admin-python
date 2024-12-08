from rest_framework.serializers import CharField
import markdown


class MarkdownField(CharField):
    # TODO: Создать MD editor для DRF
    def to_representation(self, value):
        return markdown.markdown(value)

    def to_internal_value(self, data):
        return str(data)