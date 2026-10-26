
from validators.general_validator import GeneralValidator
from exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError

class UserValidator:

    def __init__(self, general_validator: GeneralValidator) -> None:
        self.gv = general_validator

    def validate_username(self, username: str) -> str:
        self.gv.validate_blank_input(username=username)

        if any(char.isspace() for char in username):
            raise ValidationError('username cannot contain space')

        if len(username) < 8:
            raise ValidationError('username too short. minimum 8 characters required')
        
        elif len(username) > 128:
            raise ValidationError('username too long. maximum 128 characters allowed')
        
        return username

    def validate_email(self, email: str) -> str:
        self.gv.validate_blank_input(email=email)

        try:
            result = validate_email(email.strip(), check_deliverability=False)
            return result.normalized

        except EmailNotValidError:
            raise ValidationError('invalid email')

            

    def validate_password(self, password: str) -> str:

        self.gv.validate_blank_input(password=password)

        if any(char.isspace() for char in password):
            raise ValidationError('password cannot contain space')

        if len(password) < 4:
            raise ValidationError('password too short')
        
        elif len(password) > 16:
            raise ValidationError('password too long')

        return password

        