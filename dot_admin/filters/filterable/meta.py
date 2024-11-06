from django.db import models


class FilterableMetaclass(type):
    def __new__(cls, name, bases, dct):
        if 'FilterField' in dct:
            dct['_filter_field'] = dct['FilterField']
        return super().__new__(cls, name, bases, dct)


class FilterableMeta(FilterableMetaclass, models.base.ModelBase):
    pass
