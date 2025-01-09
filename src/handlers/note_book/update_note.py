from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book

@catch
def update_note(args: List[str]):
   if len(args) < 2:
        raise WrongArgumentsNumberException("You must provide both a title and text")
   title, *rest = args
   new_text = " ".join(rest)
   note = note_book.find_note(title)
   if note:
       note_book.update_note(title, new_text)
       print(f"Note with title - {title} updated successfully.",note)
   else:
        raise KeyError(f"Note with title - {title} does not exist.")