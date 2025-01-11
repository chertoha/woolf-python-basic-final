from src.models.field import Field
from src.utils.patterns import phone_pattern
import re


class Phone(Field):

    def __init__(self, value: str) -> None:
        self.__validate(value)
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)

    def __validate(self, value):
        if not bool(re.match(phone_pattern, value)):
            raise ValueError("Not valid phone! Must be 10 digits")
