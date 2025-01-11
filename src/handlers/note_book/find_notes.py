from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book

@catch
def find_notes(args: List[str]):
    if len(args) != 1:
        raise WrongArgumentsNumberException(1)
       
    title = args[0]
    notes = note_book.find_notes_by_partial_title(title)
    if len(notes) != 0:
        print(notes)
    else:
        raise KeyError(f"Note with title - {title} does not exist.")

         
    
