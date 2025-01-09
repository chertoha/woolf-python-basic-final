from typing import List
from src.models.contact_book.birthday import Birthday
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book


@catch
def add_birthday(args: List[str]):

    if (len(args) < 2):
        raise WrongArgumentsNumberException(
            f"Wrong number of arguments in command!, should be at least 2")

    name, birthday = args

    record = contact_book.find_record(name)

    if record == None:
        raise KeyError(f"Record with name {name} doesn't exist")

    record.birthday = Birthday(birthday)

    print(f"Birthday successfully changed for {birthday}")
