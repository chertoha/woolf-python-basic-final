from collections import UserList
from typing import List
from .record import Record


class ContactBook(UserList[Record]):

    def add_record(self, record: Record) -> None:
        pass

    def retrieve_contacts(self, searched_value: str = "") -> List:
        return []

    def remove_record(self, searched_name: str) -> None:
        pass

    def find_record(self, searched_name: str) -> Record | None:
        pass
