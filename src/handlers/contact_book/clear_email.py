from typing import List
from src.decorators.catch import catch
from src.decorators.confirm import confirm


@catch
@confirm("Are you sure you want to clear email?")
def clear_email(args: List[str]):
    print("clear_email")
