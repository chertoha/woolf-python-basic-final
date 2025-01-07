from typing import List
from src.decorators.catch import catch


@catch
def add_note(args: List[str]):
    print("add_note")
