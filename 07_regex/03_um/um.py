"""
CS50P Problem Set 7: Regular, um, Expressions

Count the number of times "um" appears
as a standalone word, case-insensitively.
"""

import re

PATTERN = r"\bum\b"


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(PATTERN, s.strip(), re.IGNORECASE):
        return len(matches)
    return 0


if __name__ == "__main__":
    main()
