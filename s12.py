import datetime
import random


def get_birthdays(number_of_birthdays):
    birthdays = []
    for _ in range(number_of_birthdays):
        start_of_year = datetime.date(2023, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


# print(get_birthdays(23))

