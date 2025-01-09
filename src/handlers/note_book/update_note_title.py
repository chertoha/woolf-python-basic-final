from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book


@catch
def update_note_title(args: List[str]):
    if len(args) != 2:
        raise WrongArgumentsNumberException("You must provide both a title and text")
    old_title, new_title = args
    note = note_book.find_note(old_title)
    note_new_title = note_book.find_note(new_title)
    
    if note_new_title:
        raise KeyError(f"New title - {new_title} already exists")
    elif note:
        note_book.update_note_title(old_title, new_title)
        print(f"Title in note - updated on {new_title} successfully",note)
    else:
        raise KeyError(f"Note with title - {old_title} does not exist.")
