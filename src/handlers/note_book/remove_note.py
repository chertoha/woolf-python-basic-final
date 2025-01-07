from typing import List
from src.decorators.catch import catch


@catch
def remove_note(args: List[str]):
    print("remove_note")
