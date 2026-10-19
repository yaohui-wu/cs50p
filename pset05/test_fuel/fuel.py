def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            fuel = gauge(percent)
            print(fuel)
        except (ValueError, ZeroDivisionError):
            print(
                "Numerator must be a non-negative integer "
                "and denominator must be a larger positive integer"
            )
        else:
            break


def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator, denominator = int(numerator), int(denominator)
    if denominator == 0:
        raise ZeroDivisionError
    if numerator < 0 or denominator < 0 or numerator > denominator:
        raise ValueError
    percent = round(numerator / denominator * 100)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
