from typing import List
from src.decorators.catch import catch


@catch
def add_email(args: List[str]):
    print("add_email")
