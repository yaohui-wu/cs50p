"""
CS50P Problem Set 7: Working 9 to 5

Convert a time range from 12-hour format to 24-hour format.
"""

import re

# Match an hour (1-12), optional minutes (00-59), and AM/PM
TIME_PATTERN = r"([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)"


def main():
    """
    Prompt for a time range in 12-hour format
    and print it in 24-hour format.
    """
    print(convert(input("Hours: ")))


def convert(s):
    """Convert a 12-hour time range to 24-hour format."""
    start, end = s.split(" to ")
    start_time = convert_time(start.strip())
    end_time = convert_time(end.strip())
    return f"{start_time} to {end_time}"


def convert_time(time):
    """Convert a 12-hour time to 24-hour HH:MM format."""
    if not (match := re.fullmatch(TIME_PATTERN, time)):
        raise ValueError("Invalid 12-hour time format")
    # Extract time components from regex
    hour, minute, am_pm = match.groups()
    hour = int(hour)
    # Default minutes to zero if not provided
    if minute is None:
        minute = 0
    else:
        minute = int(minute)
    # Midnight becomes 00; noon remains 12
    if am_pm == "AM" and hour == 12:
        hour = 0
    elif am_pm == "PM" and hour != 12:
        hour += 12
    # Format the result to 24-hour HH:MM format
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
