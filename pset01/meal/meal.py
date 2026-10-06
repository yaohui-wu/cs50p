def main():
    # TODO
    time = input("What time is it? ")
    hours = convert(time)
    meal = meal_time(hours)
    if meal is not None:
        print(f"{meal} time")


def convert(time):
    # TODO
    hours, minutes = time.split(":")
    hours, minutes = float(hours), float(minutes)
    hours += minutes / 60
    return hours


def meal_time(hours):
    meal = None
    if 7 <= hours <= 8:
        meal = "breakfast"
    elif 12 <= hours <= 13:
        meal = "lunch"
    elif 18 <= hours <= 19:
        meal = "dinner"
    return meal


if __name__ == "__main__":
    main()
