from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book

@catch
def remove_tags(args: List[str]):
    if len(args) != 2:
        WrongArgumentsNumberException(2)
    title, tag = args
    note = note_book.find_note(title)
    if note:
        old_tag = note.remove_tag(tag)
        if old_tag:
            print(f"Tag - {tag} successfully deleted.", note)
        else:
            print(f"Tag - {tag} doesn't exist")
    else:
        raise KeyError(f"Note with title - {title} doesn't exist")
