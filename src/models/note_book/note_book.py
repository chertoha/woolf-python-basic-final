from typing import List
from .note import Note


class NoteBook:

    def __init__(self) -> None:
        self.__notes: List[Note] = []

    def add_note(self, title: str, text: str) -> None:
        if not title or not text:
            raise ValueError("Title or text cannot be empty")
        if any((note.title == title for note in self.__notes)):
            raise KeyError(f"This title - {title} already exists")
        
        self.__notes.append(Note(title, text))
       

    def find_note(self, searched_title: str):
        note = next((note for note in self.__notes if note.title == searched_title), None)

        if note:
            return note
        else:
            raise ValueError(f"Note with title - {searched_title} not exist")

    def remove_note(self, searched_title: str):
        for index, note in enumerate(self.__notes):
            if note.title == searched_title:
                del self.__notes[index]
                return f"Note with title - {searched_title} removed successfully."
            
        raise ValueError(f"Note with title - {searched_title} does not exist")

    def update_note(self, searched_title: str, new_text: str):
        if not searched_title or not new_text:
            raise ValueError("Title and new text cannot be empty")
        
        for  note in self.__notes:
            if note.title == searched_title:
                note.text = new_text
                return f"Note with title - {searched_title} updated successfully."
            
        raise KeyError(f"Note with title - {searched_title} does not exist.")
                    
            

    def update_note_title(self, old_title: str, new_title: str):
        if not old_title or not new_title:
            raise ValueError("Old title or new title cannott be empty")
        
        if any(note.title == new_title for note in self.__notes):
            raise KeyError(f"New title - {new_title} already exists")
        
        for note in self.__notes:
            if note.title == old_title:
                note.title == new_title
                return f"Title in note - updated on {new_title} successfully"
        raise KeyError(f"Note with title - {old_title} does not exist.")
