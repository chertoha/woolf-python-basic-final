from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book
from src.models.note_book.tag import Tag


@catch
def add_tags(args: List[str]):
    if len(args) < 2:
        WrongArgumentsNumberException(2)
    title, *tags = args
    note = note_book.find_note(title)
    if note:
        note.add_tags(tags)
        print(f"Tags - '{tags}' successfully added.")

    else:
        raise KeyError(f"Note with title - {title} doesn't exist")
