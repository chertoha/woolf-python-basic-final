from typing import List
from src.decorators.catch import catch


@catch
def add_contact(args: List[str]):
    print("add_contact")
