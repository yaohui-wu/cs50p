def main():
    dollars_str = input("How much was the meal? ")
    dollars = dollars_to_float(dollars_str)
    percent = input("What percentage would you like to tip? ")
    percent_decimal = percent_to_float(percent)
    tip = dollars * percent_decimal
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d.removeprefix("$"))
    return dollars


def percent_to_float(p):
    percent = p.removesuffix("%")
    percent_decimal = float(percent) / 100
    return percent_decimal


if __name__ == "__main__":
    main()
