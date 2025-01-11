from src.models.contact_book.contact_book import ContactBook
from src.models.note_book.note_book import NoteBook


class Organizer:

    def __init__(self) -> None:
        self.note_book = NoteBook()
        self.contact_book = ContactBook()

    def __getstate__(self) -> object:
        contact_book_state = self.contact_book.get_dump_state()
        note_book_state = self.note_book.get_dump_state()
        return {"contact_book": contact_book_state, "note_book": note_book_state}

    def __setstate__(self, state):
        self.note_book = NoteBook()
        self.contact_book = ContactBook()

        contact_book_state = state["contact_book"]
        note_book_state = state["note_book"]

        self.contact_book.set_dump_state(contact_book_state)
        self.note_book.set_dump_state(note_book_state)
