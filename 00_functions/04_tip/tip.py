def main() -> None:
    dollars_text = input("How much was the meal? ")
    dollars = dollars_to_float(dollars_text)
    percent_text = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent_text)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    dollars = float(d.removeprefix("$"))
    return dollars


def percent_to_float(p: str) -> float:
    percent_number = p.removesuffix("%")
    percent = float(percent_number) / 100
    return percent


if __name__ == "__main__":
    main()
