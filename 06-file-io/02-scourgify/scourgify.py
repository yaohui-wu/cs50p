"""
CS50P Problem Set 6: Scourgify

Split full names in a CSV file into separate first and last names
in a new file.
"""

import csv
import sys


def main() -> None:
    in_filename, out_filename = get_filenames(sys.argv[1:])
    try:
        convert(in_filename, out_filename)
    except FileNotFoundError:
        sys.exit(f"Could not read {in_filename}")


def get_filenames(args: list[str]) -> tuple[str, str]:
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    if len(args) > 2:
        sys.exit("Too many command-line arguments")

    in_filename, out_filename = args[0], args[1]

    if not in_filename.endswith(".csv"):
        sys.exit("Input is not a CSV file")
    if not out_filename.endswith(".csv"):
        sys.exit("Output is not a CSV file")
    return in_filename, out_filename


def convert(in_filename: str, out_filename: str) -> None:
    with (
        open(in_filename, "r", encoding="utf-8") as in_file,
        open(out_filename, "w", encoding="utf-8") as out_file,
    ):
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
