from src.models.field import Field
from src.utils.patterns import email_pattern
import re


class Email(Field):

    def __init__(self, value: str) -> None:
        self.__validate(value)
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)

    def __validate(self, value):
        if not bool(re.match(email_pattern, value)):
            raise ValueError("Not valid email!")
