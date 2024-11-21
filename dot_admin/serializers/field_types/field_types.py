from abc import ABC


class FieldType(ABC):
    field_type: str
    context_type: str


class BooleanFieldType(FieldType):
    field_type = 'boolean'
    context_type = None


class CharFieldType(FieldType):
    field_type = 'string'
    context_type = None


class ChoiceFieldType(FieldType):
    field_type = 'string'
    context_type = 'choices'


class DateFieldType(FieldType):
    field_type = 'string'
    context_type = 'date'


class DateTimeFieldType(FieldType):
    field_type = 'string'
    context_type = 'date-time'


class DecimalFieldType(FieldType):
    field_type = 'number'
    context_type = 'float'


class DictFieldType(FieldType):
    field_type = 'object'
    context_type = None


class DurationFieldType(FieldType):
    field_type = 'string'
    context_type = 'duration'


class EmailFieldType(FieldType):
    field_type = 'string'
    context_type = 'email'


class FileFieldType(FieldType):
    field_type = 'string'
    context_type = 'file'


class FilePathFieldType(FieldType):
    field_type = 'string'
    context_type = 'file-path'


class FloatFieldType(FieldType):
    field_type = 'number'
    context_type = 'float'


class HiddenFieldType(FieldType):
    field_type = 'string'
    context_type = 'hidden'


class HStoreFieldType(FieldType):
    field_type = 'object'
    context_type = 'hstore'


class ImageFieldType(FieldType):
    field_type = 'string'
    context_type = 'image'


class IntegerFieldType(FieldType):
    field_type = 'number'
    context_type = None


class IPAddressFieldType(FieldType):
    field_type = 'string'
    context_type = 'ipv4'


class JSONFieldType(FieldType):
    field_type = 'object'
    context_type = 'json'


class ListFieldType(FieldType):
    field_type = 'array'
    context_type = None


class ModelFieldType(FieldType):
    field_type = 'object'
    context_type = 'model'


class MultipleChoiceFieldType(FieldType):
    field_type = 'array'
    context_type = 'multiple-choice'


class NullBooleanFieldType(FieldType):
    field_type = 'boolean'
    context_type = 'null-boolean'


class PrimaryKeyRelatedFieldType(FieldType):
    field_type = 'string'
    context_type = 'primary-key-related'


class ReadOnlyFieldType(FieldType):
    field_type = 'string'
    context_type = 'read-only'


class RegexFieldType(FieldType):
    field_type = 'string'
    context_type = 'regex'


class SerializerMethodFieldType(FieldType):
    field_type = 'string'
    context_type = 'serializer-method'


class SlugFieldType(FieldType):
    field_type = 'string'
    context_type = 'slug'


class TimeFieldType(FieldType):
    field_type = 'string'
    context_type = 'time'


class URLFieldType(FieldType):
    field_type = 'string'
    context_type = 'url'


class UUIDFieldType(FieldType):
    field_type = 'string'
    context_type = 'uuid'
