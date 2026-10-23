
from exceptions import ValidationError

class GeneralValidator:

    def __init__(self):
        pass

    def validate_blank_input(self, **texts) -> None:
        for key, value in texts.items():
            if not isinstance(value, str) and not value.strip():
                raise ValidationError(f"{key} cannot be empty")

    def validate_ids(self, **ids) -> None:
        for key, value in ids.items():
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValidationError(f"{key} not an integer")

