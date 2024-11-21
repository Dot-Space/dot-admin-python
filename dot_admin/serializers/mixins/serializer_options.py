import dataclasses
from rest_framework.fields import empty
from dot_admin.serializers.field_types import FIELD_TYPES


@dataclasses.dataclass
class FieldSchemaDto:
    field_type: str
    context_type: str | None
    required: bool
    allow_null: bool
    choices: list | None
    default: any
    read_only: bool
    write_only: bool
    label: str | None
    source: str | None


    def to_representation(self):
        return {
            'type': self.field_type,
            'context': self.context_type,
            'required': self.required,
            'allow_null': self.allow_null,
            'choices': self.choices,
            'default': self.default,
            'read_only': self.read_only,
            'write_only': self.write_only,
            'label': self.label,
            'source': self.source,
        }


class SchemaGeneratorMixin:
    """
    Миксин для генерации схемы сериализатора.
    """
    def get_fields_schema(self) -> dict[str, dict]:
        return dict(
            (
                field_name, 
                FieldSchemaDto(
                    field_type=FIELD_TYPES[field_instance.__class__.__name__].field_type,
                    context_type=FIELD_TYPES[field_instance.__class__.__name__].context_type,
                    required=field_instance.required,
                    allow_null=field_instance.allow_null,
                    choices=getattr(field_instance, 'choices', None),
                    default=None if field_instance.default is empty else field_instance.default,
                    read_only=field_instance.read_only,
                    write_only=field_instance.write_only,
                    label=field_instance.label,
                    source=field_instance.source,
                ).to_representation()
            )
            for field_name, field_instance in self.get_fields().items()
        )
