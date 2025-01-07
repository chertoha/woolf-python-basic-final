from typing import List
from src.decorators.catch import catch


@catch
def find_contacts(args: List[str]):
    print("find_contacts")
