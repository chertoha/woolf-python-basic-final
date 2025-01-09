from typing import List
from datetime import datetime, timedelta
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.decorators.catch import catch
from src.models.organizer import contact_book


@catch
def show_birthdays(args: List[str]):

    if len(args) < 1:
        raise WrongArgumentsNumberException(
            "Wrong number of arguments. You need to specify the number of days."
        )

    try:
        days = int(args[0])
    except ValueError:
        raise ValueError("The number of days must be an integer.")


    today = datetime.today()
    end_date = today + timedelta(days=days)


    upcoming_birthdays = []
    for record in contact_book:
        if record.birthday:
            birthday_this_year = record.birthday.replace(year=today.year)
            if today <= birthday_this_year <= end_date:
                upcoming_birthdays.append(record.name)

    # Виведення результату
    if upcoming_birthdays:
        print("Upcoming birthdays:")
        for name in upcoming_birthdays:
            print(f"- {name}")
    else:
        print("No birthdays in the specified range.")

