from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book
from src.exceptions.non_existed_record_exception import NonExistedException


@catch
def clear_address(args: List[str]):
    if (len(args) < 1):
        raise WrongArgumentsNumberException(1)

    name, = args

    record = contact_book.find_record(name)

    if record == None:
        raise NonExistedException(name)

    record.address = None

    print("Address successfully cleared")
