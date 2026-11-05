"""
CS50P Problem Set 7: Regular, um, Expressions

Count the number of times "um" appears
as a standalone word, case-insensitively.
"""

import re

UM = r"\bum\b"  # standalone word "um"


def main() -> None:
    print(count(input("Text: ")))


def count(s: str) -> int:
    if matches := re.findall(UM, s.strip(), re.IGNORECASE):
        return len(matches)
    return 0


if __name__ == "__main__":
    main()
