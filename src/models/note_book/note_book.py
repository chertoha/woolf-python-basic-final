from typing import List
from .note import Note


class NoteBook:

    def __init__(self) -> None:
        self.__notes: List[Note] = []

    def add_note(self, data: Note) -> None:
        self.__notes.append(data)
       

    def find_note(self, searched_title: str):
        return next((note for note in self.__notes if note.title == searched_title), None)
        


    def remove_note(self, searched_title: str):
        for index, note in enumerate(self.__notes):
            if note.title == searched_title:
                del self.__notes[index]
                return True
        return False
            

    def update_note(self, searched_title: str, new_text: str):
        for note in self.__notes:
            if note.title == searched_title:
                note.text = new_text
                
                    
            

    def update_note_title(self, old_title: str, new_title: str):
        for note in self.__notes:
            if note.title == old_title:
                note.title = new_title
    
    def get_dump_state(self):
        state = []

        for note in self.__notes:
            title = note.title
            text = note.text
            tags = note.get_tags()

            state.append({"title": title, "text": text, "tags": tags})

        return state

    def set_dump_state(self, state):
        for item in state:
            note = Note(item["title"], item["text"])
            note.add_tag(" ".join(item["tags"]))
            self.add_note(note)
        
