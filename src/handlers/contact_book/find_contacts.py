from typing import List
from src.helpers.logger import Logger
from src.decorators.catch import catch
from src.models.organizer import contact_book
from pprint import pprint


@catch
def find_contacts(args: List[str]):

    query = args[0] if len(args) >= 1 else ""

    records = contact_book.retrieve_contacts(query)

    if len(records) != 0:
        contact_book.show_records(records)
    else:
        Logger.warning(f"Nothing found for query '{query}'")
