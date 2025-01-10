from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book

@catch
def add_tags(args: List[str]):
    if len(args) != 2:
        WrongArgumentsNumberException(2)
    title, new_tag = args
    note = note_book.find_note(title)
    if note:
       note.add_tag(new_tag)
       print(f"Tag - '{new_tag}' successfully added.", note)
       
    else:
        raise KeyError(f"Note with title - {title} doesn't exist")
   

