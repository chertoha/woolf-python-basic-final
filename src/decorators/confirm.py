from src.exceptions.wrong_command_exception import WrongCommandException
from functools import wraps
from typing import Callable, Optional


def confirm(message: Optional[str] = "Are you sure, you want to delete?"):
    def decorator(func: Callable):

        @wraps(func)
        def inner(*args, **kwargs):
            while True:
                response = input(f"{message}, Y/N: ")

                if response.lower() == "y":
                    return func(*args, **kwargs)
                elif response.lower() == "n":
                    return
                else:
                    print("Invalid input. Please enter Y or N.")
        return inner
    return decorator
