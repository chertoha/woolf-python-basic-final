from typing import List
from src.decorators.catch import catch


@catch
def clear_address(args: List[str]):
    print("clear_address")
