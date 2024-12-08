from rest_framework.serializers import CharField
import markdown


class MarkdownField(CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = 'markdown'

    def to_representation(self, value):
        return markdown.markdown(value)

    def to_internal_value(self, data):
        return str(data)