from typing import List
from .tag import Tag


class Note():
    def __init__(self, title: str, text: str) -> None:
        self.__title = None
        self.__text = None

        self.__tags: set[Tag] = set()
        self.title = title
        self.text = text

    def __str__(self):
        return f"Note[title={self.title}, text={self.text}, tags={self.__tags}]"

    def __repr__(self):
        return f"Note[title={self.title}, text={self.text}, tags={self.__tags}]"
    
    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, new_tag: str):
        if not new_tag:
            raise ValueError("Tag cannot be empty")
        self.__tags = new_tag


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title: str):

        if not new_title:
            raise ValueError("Title cannot be empty")

        self.__title = new_title

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text: str):
        self.__text = new_text

    def add_tag(self, new_tag: str):
        self.__tags.add(("#" + new_tag))

    def remove_tag(self, searched_tag: str):
        for tag in self.__tags:
            if tag == ("#" + searched_tag):
                self.__tags.remove(tag)
                return True
        return False
    
    
    

