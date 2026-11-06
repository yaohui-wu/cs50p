"""
CS50P Problem Set 6: Pizza Py

Read a CSV file in Pinocchio's format to ouput a prettier menu table.
"""

import csv
import sys

from tabulate import tabulate


def main() -> None:
    filename = get_filename(sys.argv[1:])

    try:
        table = read_table(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def get_filename(args: list[str]) -> str:
    if len(args) < 1:
        sys.exit("Too few command-line arguments")
    elif len(args) > 1:
        sys.exit("Too many command-line arguments")

    filename = args[0]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    return filename


def read_table(filename: str) -> list[list[str]]:
    table = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

    return table


if __name__ == "__main__":
    main()
