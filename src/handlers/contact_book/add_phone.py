from typing import List
from src.decorators.catch import catch


@catch
def add_phone(args: List[str]):
    print("add_phone")
