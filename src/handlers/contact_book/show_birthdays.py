from typing import List
from src.decorators.catch import catch


@catch
def show_birthdays(args: List[str]):
    print("show_birthdays")
