from typing import List
from src.decorators.catch import catch


@catch
def add_tags(args: List[str]):
    print("add_tags")
