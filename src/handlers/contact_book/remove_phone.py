from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def remove_phone(args: List[str]):

    if len(args) < 2:
        raise WrongArgumentsNumberException("Wrong number of arguments. Command should include name and phone.")
    
    name, phone = args

    record = contact_book.find_record(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' not found.")
    
    if not record.find_phone(phone):
        raise ValueError(f"Phone number '{phone}' not found in contact '{name}'.")
    
    record.remove_phone(phone)

    print(f"Phone number '{phone}' removed from contact '{name}'.")