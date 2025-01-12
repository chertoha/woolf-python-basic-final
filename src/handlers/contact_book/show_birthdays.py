from typing import List
from datetime import datetime, timedelta
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book
from src.helpers.logger import Logger

@catch
def show_birthdays(args: List[str]):
    if len(args) < 1:
        raise WrongArgumentsNumberException("Please specify the number of days.")

    try:
        days = int(args[0])
    except ValueError:
        raise ValueError("The number of days must be an integer.")

    # Отримуємо дні народження
    upcoming_birthdays = contact_book.get_upcoming_birthdays(days)

    # Виводимо результат
    if upcoming_birthdays:
        print("Upcoming birthdays:")
        for birthday in upcoming_birthdays:
            print(
                f"- {birthday['name']} (Birthday: {birthday['birthday_date']}, "
                f"Congratulation Date: {birthday['congratulation_date']})"
            )
    else:
        Logger.warning("No birthdays in the specified range.")
