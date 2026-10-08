def main():
    percent = get_percent()
    fuel = round(percent)
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_percent():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator < 0 or denominator < 0:
                raise ValueError
            if numerator > denominator:
                raise ValueError
            percent = numerator / denominator * 100
            return percent
        except (ZeroDivisionError, ValueError):
            print(
                "Numerator must be a non-negative integer "
                "and denominator must be a larger positive integer"
            )


if __name__ == "__main__":
    main()
