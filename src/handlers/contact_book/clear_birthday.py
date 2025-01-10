from typing import List
from src.decorators.confirm import confirm
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import contact_book
from src.exceptions.non_existed_record_exception import NonExistedException


@catch
@confirm("Are you sure you want to clear birthday?")
def clear_birthday(args: List[str]):
    if (len(args) < 1):
        raise WrongArgumentsNumberException(1)

    name, = args

    record = contact_book.find_record(name)

    if record == None:
        raise NonExistedException(name)

    record.birthday = None

    print("Birthday successfully cleared")
