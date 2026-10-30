"""
CS50P Problem Set 8: CS50 Shirtificate

Generate a customized CS50 shirtificate PDF with the user's name.
"""

import sys


def main() -> None:
    """
    Prompt for the user's name
    and save a customized CS50 shirtificate PDF.
    """
    # TODO
    name = input("Name: ").strip()
    if not name:  # Reject blank input
        sys.exit("Invalid name")
    name = name.title()
    ...


if __name__ == "__main__":
    main()
