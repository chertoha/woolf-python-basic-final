from typing import List
from .note import Note


class NoteBook:

    def __init__(self) -> None:
        self.__notes: List[Note] = []

    def add_note(self, title: str, text: str) -> None:
        pass

    def find_note(self, searched_title: str):
        pass

    def remove_note(self, searched_title: str):
        pass

    def update_note(self, searched_title: str, new_text: str):
        pass

    def update_note_title(self, old_title: str, new_title: str):
        pass
