def main():
    percent = get_percent()
    fuel = round(percent)
    if fuel < 1:
        print("E")
    elif fuel > 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_percent():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            if numerator.isdigit() and denominator.isdigit():
                numerator = int(numerator)
                denominator = int(denominator)
                valid_nums = (
                    numerator >= 0
                    and denominator > 0
                    and numerator <= denominator
                )
                if valid_nums:
                    percent = numerator / denominator * 100
                    return percent
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
