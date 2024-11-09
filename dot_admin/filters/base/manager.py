from django.db import models

from .queryset import FilterableQuerySet


class FilterableManager(models.Manager):
    def get_queryset(self):
        return FilterableQuerySet(self.model, using=self._db)
