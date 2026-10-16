import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")


if __name__ == "__main__":
    main()
