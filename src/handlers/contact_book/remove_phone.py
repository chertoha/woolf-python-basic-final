from typing import List
from src.decorators.catch import catch


@catch
def remove_phone(args: List[str]):
    print("remove_phone")
