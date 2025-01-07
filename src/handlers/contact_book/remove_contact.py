from typing import List
from src.decorators.catch import catch


@catch
def remove_contact(args: List[str]):
    print("remove_contact")
