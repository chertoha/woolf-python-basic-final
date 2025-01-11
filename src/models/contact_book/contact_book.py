from collections import UserList
from typing import List

from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from .record import Record


class ContactBook(UserList[Record]):

    def add_record(self, record: Record) -> None:
        self.data.append(record)

    def retrieve_contacts(self, searched_value: str = "") -> List:

        if searched_value == "":
            return self.data

        res = []

        for record in self.data:

            name = str(record.name).lower()
            email = str(record.email).lower(
            ) if record.email is not None else ""
            address = str(record.address).lower(
            ) if record.address is not None else ""
            birthday = str(
                record.birthday).lower() if record.birthday is not None else ""
            phones = [str(phone).lower() for phone in record.phones]

            if (searched_value.lower() in name or
                    searched_value in email or
                    searched_value in address or
                    searched_value in birthday or
                    searched_value in phones):

                res.append(record)

        return res

    def remove_record(self, searched_name: str) -> None:
        record = self.find_record(searched_name)
        if record:
            self.data.remove(record)
        else:
            raise ValueError(f"Contact with name '{searched_name}' not found.")

    def find_record(self, searched_name: str) -> Record | None:
        return next((record for record in self.data if str(record.name) == searched_name), None)

    def get_dump_state(self):
        state = []

        for record in self.data:
            name = str(record.name)
            address = str(
                record.address) if record.address is not None else None
            email = str(record.email) if record.email is not None else None
            birthday = str(
                record.birthday) if record.birthday is not None else None
            phones = [str(phone) for phone in record.phones]

            state.append(
                {"name": name, "phones": phones, "birthday": birthday, "address": address, "email": email})

        return state

    def set_dump_state(self, state):

        for contact in state:
            record = Record(contact["name"])

            if contact["birthday"] is not None:
                record.birthday = Birthday(contact["birthday"])

            if contact["email"] is not None:
                record.email = Email(contact["email"])

            if contact["address"] is not None:
                record.address = Address(contact["address"])

            for phone in contact["phones"]:
                record.add_phone(phone)

            self.add_record(record)

    def show_records(self, records: List[Record]):

        for record in records:
            print(record)
