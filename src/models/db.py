import pickle

from src.models.organizer_class import Organizer


class Database:

    def __init__(self, filename: str = "data/organizer.pkl") -> None:
        self.__filename = filename

    def save_data(self, organizer: Organizer) -> None:
        with open(self.__filename, "wb") as file:
            pickle.dump(organizer, file)

    def load_data(self):
        try:
            with open(self.__filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Organizer()
