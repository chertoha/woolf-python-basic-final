from typing import List
from src.decorators.catch import catch


@catch
def clear_email(args: List[str]):
    print("clear_email")
