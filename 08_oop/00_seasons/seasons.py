"""
CS50P Problem Set 8: Seasons of Love

Prompt the user for their birthdate in YYYY-MM-DD format
and print the user's age in minutes using English words.
"""

import re
import sys
from datetime import date

import inflect

DATE_FORMAT = r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60


def main() -> None:
    """Get birthdate from user input and print their age in minutes."""
    birthdate_str = input("Date of Birth: ").strip()
    birthdate = parse_date(birthdate_str)
    today = date.today()
    if today < birthdate:  # Reject future birthdate
        sys.exit("Invalid Date")
    minutes = calculate_minutes(birthdate, today)
    minutes_words = num_to_words(minutes)
    print(f"{minutes_words.capitalize()} minutes")


def parse_date(date_str: str) -> date:
    """Validate and parse a date string in YYYY-MM-DD format."""
    try:
        if not re.fullmatch(DATE_FORMAT, date_str):
            sys.exit("Invalid date")
        return date.fromisoformat(date_str)
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes(start_date: date, end_date: date) -> int:
    """Calculate the number of minutes between two dates."""
    delta = end_date - start_date
    minutes = delta.days * HOURS_IN_DAY * MINUTES_IN_HOUR
    return minutes


def num_to_words(num: int) -> str:
    """Convert an integer to English words, omitting "and"."""
    engine = inflect.engine()
    return engine.number_to_words(num, andword="")


if __name__ == "__main__":
    main()
