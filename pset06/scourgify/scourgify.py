"""
CS50P Problem Set 6: Scourgify

Split full names in a CSV file into separate first and last names
in a new file.
"""

import csv
import sys


def main():
    args = sys.argv[1:]
    in_filename, out_filename = get_filenames(args)
    try:
        convert(in_filename, out_filename)
    except FileNotFoundError:
        sys.exit(f"Could not read {in_filename}")


def get_filenames(args):
    args_len = len(args)
    if args_len < 2:
        sys.exit("Too few command-line arguments")
    elif args_len > 2:
        sys.exit("Too many command-line arguments")
    in_filename, out_filename = args[0], args[1]
    if not in_filename.endswith(".csv"):
        sys.exit("Input is not a CSV file")
    if not out_filename.endswith(".csv"):
        sys.exit("Output is not a CSV file")
    return in_filename, out_filename


def convert(in_filename, out_filename):
    with open(in_filename) as in_file, open(out_filename, "w") as out_file:
        reader = csv.DictReader(in_file)
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            first, last = first.strip(), last.strip()
            student = {"first": first, "last": last, "house": row["house"]}
            writer.writerow(student)


if __name__ == "__main__":
    main()
