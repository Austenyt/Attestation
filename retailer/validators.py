from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


def validate_email(value):
    validator = EmailValidator()
    try:
        validator(value)
    except ValidationError:
        raise ValidationError("Некорректный формат email адреса.")
