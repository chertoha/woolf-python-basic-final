from typing import List
from src.decorators.catch import catch


@catch
def update_phone(args: List[str]):
    print("update_phone")
