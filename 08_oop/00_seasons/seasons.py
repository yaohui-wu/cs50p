"""
CS50P Problem Set 8: Seasons of Love

Prompt the user for their birthdate in YYYY-MM-DD format
and print their age in minutes using English words.
"""

import datetime as dt
import re
import sys

import inflect

DATE_FORMAT = r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
SECONDS_IN_MINUTE = 60


def main():
    """Get birthdate from user input and print their age in mintues."""
    # TODO
    dob = input("Date of Birth: ").strip()
    birthdate = parse_date(dob)
    today = dt.date.today()
    minutes = calculate_minutes(birthdate, today)
    minutes_words = num_to_words(minutes)
    print(f"{minutes_words} minutes")


def parse_date(date_str):
    """Validate and parse a date string in YYYY-MM-DD format."""
    try:
        if not re.fullmatch(DATE_FORMAT, date_str):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")
        return dt.date.fromisoformat(date_str)
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes(start_date, end_date):
    """Caculate minutes between two date objects."""
    delta = end_date - start_date
    seconds = delta.total_seconds()
    minutes = seconds / SECONDS_IN_MINUTE
    return minutes


def num_to_words(num):
    num = round(num)
    p = inflect.engine()
    return p.number_to_words(num)


if __name__ == "__main__":
    main()
