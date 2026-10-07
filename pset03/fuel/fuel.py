def main():
    # TODO
    percent = get_percent()


def get_percent():
    # TODO
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            if numerator.isdigit() and denominator.isdigit():
                numerator = int(numerator)
                denominator = int(denominator)
                if numerator >= 0 and denominator > 0 and numerator <= denominator:
                    percent = numerator / denominator * 100
                    return percent
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
