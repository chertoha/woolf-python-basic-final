from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book


@catch
def clear_birthday(args: List[str]):
    if (len(args) < 1):
        raise WrongArgumentsNumberException(
            f"Wrong number of arguments in command!, should be at least 1")

    name, = args

    record = contact_book.find_record(name)

    if record == None:
        raise KeyError(f"Record with name {name} doesn't exist")

    record.birthday = None

    print("Birthday successfully changed")
