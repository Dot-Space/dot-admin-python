from typing import Type

from django.db import models

from dot_admin.adapter.convertes.datatype import BaseDataTypeConverter


class ModelOptionsSchema:
    model: Type[models.Model]
    fields: tuple[str]

    datatype_converter: Type[BaseDataTypeConverter]

    @property
    def model_name(self):
        return self.model._meta.model_name

    @property
    def app_label(self):
        return self.model._meta.app_label

    @property
