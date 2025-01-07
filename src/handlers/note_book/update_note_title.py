from typing import List
from src.decorators.catch import catch


@catch
def update_note_title(args: List[str]):
    print("update_note_title")
