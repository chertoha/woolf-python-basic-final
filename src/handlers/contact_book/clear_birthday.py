from typing import List
from src.decorators.catch import catch


@catch
def clear_birthday(args: List[str]):
    print("clear_birthday")
