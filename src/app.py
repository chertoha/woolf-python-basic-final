import json
from src.cli.autocomplete_config import CommandCompleter, autocmplete_style
from src.cli.config import Commands
from src.models.contact_book.record import Record
from src.cli.commands import execute_command
from src.cli.parser import parse_input
from src.models.organizer import contact_book
from prompt_toolkit import PromptSession
from src.models.organizer import db
from src.models.organizer import organizer_instance


# with open('data/mock_contacts.json', 'r') as f:
#     mock_contacts = json.load(f)


def app() -> None:

    COMMANDS = [cmd.value for cmd in Commands]

    autocomplete_session = PromptSession(
        completer=CommandCompleter(COMMANDS), style=autocmplete_style)

    # for contact in mock_contacts:
    #     record = Record(contact["name"])
    #     for tel in contact["phones"]:
    #         record.add_phone(tel)

    #     contact_book.add_record(record)

    while True:
        try:
            user_input = autocomplete_session.prompt(
                "Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["exit", "quit", "end"]:
                print("Bye!")
                break

            execute_command(command, args)
            db.save_data(organizer_instance)

        except Exception as err:
            print(err)
