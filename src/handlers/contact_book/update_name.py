from typing import List
from src.decorators.catch import catch


@catch
def update_name(args: List[str]):
    print("update_name")
