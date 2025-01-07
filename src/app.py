import json
from src.models.contact_book.record import Record
from src.cli.commands import execute_command
from src.cli.parser import parse_input
from src.models.organizer import contact_book


with open('data/mock_contacts.json', 'r') as f:
    mock_contacts = json.load(f)


def app() -> None:

    for contact in mock_contacts:
        record = Record(contact["name"])
        for tel in contact["phones"]:
            record.add_phone(tel)

        contact_book.add_record(record)

    while True:
        try:
            user_input = input("Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["exit", "quit", "end"]:
                print("Bye!")
                break

            execute_command(command, args)

        except Exception as err:
            print(err)
