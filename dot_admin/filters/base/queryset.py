from django.db import models


class FilterableQuerySet(models.QuerySet):
    """
    Кастомный QuerySet для фильтруемых моделей

    Этот QuerySet позволяет фильтровать модели по значениям фильтров.
    """
    def filter_by_fields(self, **kwargs):
        queryset = self

        filter_model = getattr(self.model, '_filter_field', None)
        if filter_model is None:
            raise ValueError("Модель должна иметь мета-класс и поле FilterField, "
                             "чтобы использовать 'filter_by_fields'.")

        for filter_name, filter_values in kwargs.items():
            filter_instance = filter_model.objects.filter(code=filter_name).first()
            if filter_instance:
                queryset = queryset.filter(
                    filters__filter_class=filter_instance,
                    filters__value__in=filter_values
                )

        return queryset