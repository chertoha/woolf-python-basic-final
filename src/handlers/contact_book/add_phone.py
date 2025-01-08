from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def add_phone(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(
            f"Wrong number of arguments in command!, should be at least 2")
    
    name, phone = args

    record = contact_book.find_record(name)
    print(f"Record found: {record}")

    if record and record.find_phone(phone):
        raise ValueError(f"Contact {name} already has phone {phone}")
    
    if record is None:
        record = Record(name)
        print(f"New record created: {record}")
        record.add_phone(phone)
        contact_book.add_record(record)
        print(f"Record added to contact_book: {record}")
    else:
        record.add_phone(phone)
        print(f"Phone {phone} added to existing record {record}")

    print("add_phone completed")
