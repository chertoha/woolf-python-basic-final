from typing import List
from src.decorators.catch import catch


@catch
def update_note(args: List[str]):
    print("update_note")
