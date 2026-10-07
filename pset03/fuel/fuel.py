def main():
    # TODO


def get_percent():
    # TODO
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
        except ZeroDivisionError:
            print("Denominator cannot be zero")
        except ValueError:
            pass


if __name__ == "__main__":
    main()
