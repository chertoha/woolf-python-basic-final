from typing import List
from .config import Commands
from src.decorators.catch import catch
from src.exceptions.wrong_command_exception import WrongCommandException
from src.handlers.contact_book import *
from src.handlers.note_book import *
from src.handlers import show_help


# commands = {
#     Commands.FIND_CONTACTS: find_contacts,
#     Commands.ADD_CONTACT: add_contact,
#     Commands.REMOVE_CONTACT: remove_contact,
#     Commands.UPDATE_NAME: update_name,
#     Commands.ADD_PHONE: add_phone,
#     Commands.UPDATE_PHONE: update_phone,
#     Commands.REMOVE_PHONE: remove_phone,
#     Commands.ADD_ADDRESS: add_address,
#     Commands.CLEAR_ADDRESS: clear_address,
#     Commands.ADD_EMAIL: add_email,
#     Commands.CLEAR_EMAIL: clear_email,
#     Commands.ADD_BIRTHDAY: add_birthday,
#     Commands.CLEAR_BIRTHDAY: clear_birthday,
#     Commands.BIRTHDAYS: show_birthdays,

#     Commands.ADD_NOTE: add_note,
#     Commands.UPDATE_NOTE: update_note,
#     Commands.UPDATE_NOTE_TITLE: update_note_title,
#     Commands.REMOVE_NOTE: remove_note,
#     Commands.ADD_TAGS: add_tags,
#     Commands.REMOVE_TAGS: remove_tags,
#     Commands.FIND_NOTES: find_notes,
#     Commands.FIND_TAGS: find_tags,

#     Commands.HELP: show_help
# }


# @ catch
# def execute_command(command: str, args: List[str]):
#     if any(cmd.value == command for cmd in Commands):
#         handler = commands[Commands(command)]
#         handler(args)
#     else:
#         raise WrongCommandException()

commands = {
    Commands.FIND_CONTACTS: {"handler": find_contacts, "description": "Find contacts by a specified search query (name, email, address, birthday, or phone)."},
    Commands.ADD_CONTACT: {"handler": add_contact, "description": "Add a new contact to the contact book."},
    Commands.REMOVE_CONTACT: {"handler": remove_contact, "description": "Remove a contact from the contact book by name."},
    Commands.UPDATE_NAME: {"handler": update_name, "description": "Update the name of an existing contact."},
    Commands.ADD_PHONE: {"handler": add_phone, "description": "Add a phone number to an existing contact."},
    Commands.UPDATE_PHONE: {"handler": update_phone, "description": "Update an existing phone number for a contact."},
    Commands.REMOVE_PHONE: {"handler": remove_phone, "description": "Remove a phone number from a contact."},
    Commands.ADD_ADDRESS: {"handler": add_address, "description": "Add an address to an existing contact."},
    Commands.CLEAR_ADDRESS: {"handler": clear_address, "description": "Remove the address from a contact."},
    Commands.ADD_EMAIL: {"handler": add_email, "description": "Add an email address to an existing contact."},
    Commands.CLEAR_EMAIL: {"handler": clear_email, "description": "Remove the email address from a contact."},
    Commands.ADD_BIRTHDAY: {"handler": add_birthday, "description": "Add a birthday to an existing contact."},
    Commands.CLEAR_BIRTHDAY: {"handler": clear_birthday, "description": "Remove the birthday from a contact."},
    Commands.BIRTHDAYS: {"handler": show_birthdays, "description": "Show contacts with birthdays within a specified number of days from today."},

    Commands.ADD_NOTE: {"handler": add_note, "description": "Add a new note to the notebook."},
    Commands.UPDATE_NOTE: {"handler": update_note, "description": "Update the content of an existing note."},
    Commands.UPDATE_NOTE_TITLE: {"handler": update_note_title, "description": "Update the title of an existing note."},
    Commands.REMOVE_NOTE: {"handler": remove_note, "description": "Remove a note from the notebook."},
    Commands.ADD_TAGS: {"handler": add_tags, "description": "Add tags to an existing note."},
    Commands.REMOVE_TAGS: {"handler": remove_tags, "description": "Remove tags from an existing note."},
    Commands.FIND_NOTES: {"handler": find_notes, "description": "Search notes by content or title."},
    Commands.FIND_TAGS: {"handler": find_tags, "description": "Search notes by tags."},

    # Commands.HELP: {"handler": show_help,
    #                 "description": "Display help information for available commands."}
}


def execute_command(command: str, args: List[str]):
    if command in [cmd.value for cmd in Commands]:
        cmd_enum = Commands(command)
        handler = commands[cmd_enum]["handler"]
        handler(args)
    elif command in ["help"]:
        return
    else:
        raise WrongCommandException(
            f"Command '{command}' not recognized. Use 'help' to see available commands.")
