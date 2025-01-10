from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book
from src.decorators.confirm import confirm


@catch
@confirm()
def remove_note(args: List[str]):
    if len(args) != 1:
        raise WrongArgumentsNumberException(1)
    title = args[0]
    resp = note_book.remove_note(title)
    if resp:
        print(f"Note with this title - {title} successfully deleted.")
    else:
        print(f"Note with title - {title} does not exist.")
