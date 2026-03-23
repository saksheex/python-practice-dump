import sys
from datetime import date

import inflect


def main():
    dob_str = input("Date of Birth: ").strip()
    try:
        dob = date.fromisoformat(dob_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    if dob > today:
        sys.exit("Invalid date")

    minutes = calculate_minutes(dob, today)
    print(f"{minutes_to_words(minutes).capitalize()} minutes")


def calculate_minutes(dob: date, today: date) -> int:
    return (today - dob).days * 24 * 60


def minutes_to_words(n: int) -> str:
    p = inflect.engine()
    return p.number_to_words(n, andword="")


if __name__ == "__main__":
    main()
