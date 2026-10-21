"""
CS50P Problem Set 6: Scourgify

Split names from a CSV file into first and last names,
and write them to a new CSV file.
"""

import sys


def main():
    args = sys.argv[1:]
    input_filename, output_filename = get_filenames(args)


def get_filenames(args):
    args_len = len(args)
    if args_len < 2:
        sys.exit("Too few command-line arguments")
    elif args_len > 2:
        sys.exit("Too many command-line arguments")
    input_filename, output_filename = args[0], args[1]
    if not input_filename.endswith(".csv"):
        sys.exit("Input is not a CSV file")
    if not output_filename.endswith(".csv"):
        sys.exit("Output is not a CSV file")
    return input_filename, output_filename


if __name__ == "__main__":
    main()
