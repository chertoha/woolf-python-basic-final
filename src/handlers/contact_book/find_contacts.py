from typing import List
from src.decorators.catch import catch
from src.models.organizer import contact_book
from pprint import pprint


@catch
def find_contacts(args: List[str]):
    # temporary code
    pprint(contact_book.retrieve_contacts(), indent=4)
