from typing import List
from .address import Address
from .birthday import Birthday
from .email import Email
from .name import Name
from .phone import Phone


class Record:

    def __init__(self, name: str) -> None:

        self.__name: Name | None = None
        self.__address: Address | None = None
        self.__email: Email | None = None
        self.__birthday: Birthday | None = None
        self.__phones: List[Phone] = []

        self.name = Name(name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: Name):
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address: Address):
        self.__address = new_address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: Email):
        self.__email = new_email

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_birthday: Birthday | None):
        self.__birthday = new_birthday

    @property
    def phones(self):
        return self.__phones

    def add_phone(self, new_phone: str):
        self.__phones.append(Phone(new_phone))

    def find_phone(self, searched_phone: str) -> Phone | None:
        return next((phone for phone in self.__phones if str(phone) == searched_phone), None)
