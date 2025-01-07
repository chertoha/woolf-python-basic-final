from typing import List
from .config import Commands
from src.decorators.catch import catch
from src.exceptions.wrong_command_exception import WrongCommandException
from src.handlers.contact_book import *
from src.handlers.note_book import *
from src.handlers import show_help


commands = {
    Commands.FIND_CONTACTS: find_contacts,
    Commands.ADD_CONTACT: add_contact,
    Commands.REMOVE_CONTACT: remove_contact,
    Commands.UPDATE_NAME: update_name,
    Commands.ADD_PHONE: add_phone,
    Commands.UPDATE_PHONE: update_phone,
    Commands.REMOVE_PHONE: remove_phone,
    Commands.ADD_ADDRESS: add_address,
    Commands.CLEAR_ADDRESS: clear_address,
    Commands.ADD_EMAIL: add_email,
    Commands.CLEAR_EMAIL: clear_email,
    Commands.ADD_BIRTHDAY: add_birthday,
    Commands.CLEAR_BIRTHDAY: clear_birthday,
    Commands.BIRTHDAYS: show_birthdays,

    Commands.ADD_NOTE: add_note,
    Commands.UPDATE_NOTE: update_note,
    Commands.UPDATE_NOTE_TITLE: update_note_title,
    Commands.REMOVE_NOTE: remove_note,
    Commands.ADD_TAGS: add_tags,
    Commands.REMOVE_TAGS: remove_tags,
    Commands.FIND_NOTES: find_notes,
    Commands.FIND_TAGS: find_tags,

    Commands.HELP: show_help
}


@ catch
def execute_command(command: str, args: List[str]):
    if any(cmd.value == command for cmd in Commands):
        handler = commands[Commands(command)]
        handler(args)
    else:
        raise WrongCommandException()
