"""
CS50P Problem Set 6: Lines of Code

Count lines of code in a specified Python file,
excluding comments and blank lines.
"""

import sys


def main():
    args = sys.argv[1:]  # User arguments
    filename = get_filename(args)
    lines = get_lines(filename)


def get_filename(args):
    args_len = len(args)
    if args_len < 1:
        sys.exit("Too few command-line arguments")
    elif args_len > 1:
        sys.exit("Too many command-line arguments")
    filename = args[0]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    return filename


def get_lines(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines


if __name__ == "__main__":
    main()
