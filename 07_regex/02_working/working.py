"""
CS50P Problem Set 7: Working 9 to 5

Convert 12-hour time to 24-hour time.
"""

import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        start, end = s.split("to")
    except ValueError:
        sys.exit("Invalid 12-hour time")


if __name__ == "__main__":
    main()
