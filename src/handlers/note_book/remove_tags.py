from typing import List
from src.helpers.logger import Logger
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book
from src.decorators.confirm import confirm


@catch
@confirm("Are you sure you want to delete these tags?")
def remove_tags(args: List[str]):
    if len(args) != 2:
        WrongArgumentsNumberException(2)
    title, *tags = args
    note = note_book.find_note(title)
    if note:
        note.remove_tags(tags)
        Logger.success(f"Tag - {tags} successfully deleted.")

    else:
        raise KeyError(f"Note with title - {title} doesn't exist")
