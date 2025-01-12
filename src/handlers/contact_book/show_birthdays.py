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

    today = datetime.today().date()
    end_date = today + timedelta(days=days)

    upcoming_birthdays = []
    for record in contact_book:
        if record.birthday:
            birthday_date = record.birthday.to_datetime().date()
            birthday_this_year = birthday_date.replace(year=today.year)

            if today <= birthday_this_year <= end_date:
                upcoming_birthdays.append(f"{record.name} - {birthday_this_year.strftime('%d %B')}")

    if upcoming_birthdays:
        print("Upcoming birthdays:")
        for birthday in upcoming_birthdays:
            print(f"- {birthday}")
    else:
        Logger.warning("No birthdays in the specified range.")

