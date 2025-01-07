from typing import List
from src.decorators.catch import catch


@catch
def find_notes(args: List[str]):
    print("find_notes")
