from typing import List
from src.decorators.catch import catch
from src.models.organizer import organizer_instance
@catch
def add_note(args: List[str]):
    if len(args) > 2:
        raise ValueError("You must provide both a title and text")
    title = args[0]
    text = args[1]

    organizer_instance.note_book.add_note(title, text)
    return f"Note with title '{title}' successfully added."
