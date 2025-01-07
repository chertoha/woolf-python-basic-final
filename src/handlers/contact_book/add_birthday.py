from typing import List
from src.decorators.catch import catch


@catch
def add_birthday(args: List[str]):
    print("add_birthday")
