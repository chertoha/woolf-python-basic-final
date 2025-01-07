from typing import List
from src.decorators.catch import catch


@catch
def find_tags(args: List[str]):
    print("find_tags")
