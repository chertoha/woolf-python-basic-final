from typing import List
from src.models.contact_book.record import Record
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def remove_phone(args: List[str]):
    
    name, phone = args

    record = contact_book.find_record(name)

    if record == None:
        raise ValueError(f"There is no phone {phone} in with contact")

    contact_book.remove_phone(phone)


    print("remove_phone")
