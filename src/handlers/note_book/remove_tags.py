from typing import List
from src.decorators.catch import catch


@catch
def remove_tags(args: List[str]):
    print("remove_tags")
