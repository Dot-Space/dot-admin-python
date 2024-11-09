from .yandex_metrica.api import send_event

class YandexMetricaMixin:
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        send_event('page_view', {'url': request.path})
        return response