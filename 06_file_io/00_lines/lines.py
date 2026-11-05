"""
CS50P Problem Set 6: Lines of Code

Count the lines of code in a Python file,
excluding blank lines and comments.
"""

import sys


def main() -> None:
    args = sys.argv[1:]  # User arguments
    filename = get_filename(args)
    lines = get_lines(filename)
    count = count_lines(lines)
    print(count)


def get_filename(args: list[str]) -> str:
    args_len = len(args)
    if args_len < 1:
        sys.exit("Too few command-line arguments")
    elif args_len > 1:
        sys.exit("Too many command-line arguments")
    filename = args[0]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    return filename


def get_lines(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines


def count_lines(lines: list[str]) -> int:
    count = 0
    for line in lines:
        if is_code(line):
            count += 1
    return count


def is_code(line: str) -> bool:
    line = line.lstrip()
    if line == "" or line.startswith("\n") or line.startswith("#"):
        # Exclude blank lines and comments
        return False
    return True


if __name__ == "__main__":
    main()
