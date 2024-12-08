from rest_framework.serializers import CharField


class MarkdownField(CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = 'markdown'
