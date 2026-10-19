def main():
    # TODO


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
