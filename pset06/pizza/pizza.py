"""
CS50P Problem Set 6: Pizza Py

Read a CSV file in Pinocchio's format to ouput a prettier menu table.
"""

import sys


def main():
    args = sys.argv[1:]
    filename = get_filename(args)


def get_filename(args):
    args_len = len(args)
    if args_len < 1:
        sys.exit("Too few command-line arguments")
    elif args_len > 1:
        sys.exit("Too many command-line arguments")
    filename = args[0]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    return filename


if __name__ == "__main__":
    main()
