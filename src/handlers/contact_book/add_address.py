from typing import List
from src.decorators.catch import catch


@catch
def add_address(args: List[str]):
    print("add_address")
