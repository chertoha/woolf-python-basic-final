from typing import List
from src.decorators.catch import catch
from src.models.organizer import contact_book
from pprint import pprint


@catch
def find_contacts(args: List[str]):
    # temporary code
    searched_value = ""
    if len(args) != 0:
        searched_value = args[0]

    pprint(contact_book.retrieve_contacts(searched_value), indent=4)
