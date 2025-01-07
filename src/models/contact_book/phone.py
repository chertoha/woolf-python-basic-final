from src.models.field import Field


class Phone(Field):

    def __init__(self, value: str) -> None:
        # self.__validate(value)
        super().__init__(value)

    def __str__(self) -> str:
        return str(self._value)

    def __validate(self, value):
        if len(value) != 10:
            raise ValueError("Phone number must have 10 digits")
