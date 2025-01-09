from typing import List
from src.models.contact_book.record import Record
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def update_phone(args: List[str]):
    if len(args) < 3:
        raise WrongArgumentsNumberException(
            "Wrong number of arguments in command! Should include name, old phone, and new phone."
        )
    
    name, old_phone, new_phone, *_ = args

    record = contact_book.find_record(name)

    if record is None:
        raise KeyError(f"Contact with name '{name}' not found.")
    
    if not record.find_phone(old_phone):
        raise ValueError(f"Phone number '{old_phone}' not found in contact '{name}'.")

    if record.find_phone(new_phone):
        raise ValueError(f"Phone number '{new_phone}' already exists in contact '{name}'.")

    # for other_record in contact_book:
    #     if other_record != record and other_record.find_phone(new_phone):
    #         raise ValueError(f"The phone number '{new_phone}' is already in use by another contact.")

    record.update_phone(old_phone, new_phone)

    print(f"Phone number '{old_phone}' updated to '{new_phone}' for contact '{name}'.")
