from typing import List
from src.decorators.catch import catch


@catch
def show_help(args: List[str]):
    print("show_help")
