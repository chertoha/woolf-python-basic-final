from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def update_name(args: List[str]):
    if len(args) < 2:
        raise WrongArgumentsNumberException(
            f"Wrong number of arguments in command!, should be at least 2")
    
    old_name, new_name, *_ = args

    record = contact_book.find_record(old_name)
    if record is None:
        raise KeyError(f"Contact with name '{old_name}' not found.")
    
    existing_record = contact_book.find_record(new_name)
    if existing_record and existing_record != record:
        raise ValueError(f"The name '{new_name}' is already in the contact book. Please choose a different name.")
    
    record.update_name(new_name)


    print(f"Name updated for {new_name}.")



