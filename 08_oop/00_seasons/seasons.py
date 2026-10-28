"""
CS50P Problem Set 8: Seasons of Love

Prompt the user for their birthdate in YYYY-MM-DD format
and print their age in minutes using English words.
"""

import re
import sys
from datetime import date


def main():
    # TODO
    dob = input("Date of Birth: ")
    birthdate = parse_date(dob)


def parse_date(date_str):
    try:
        pattern = r"\d{4}-\d{2}-\d{2}"
        if not re.fullmatch(pattern, date_str):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")
        return date.fromisoformat(date_str)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
