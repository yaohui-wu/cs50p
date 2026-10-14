def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
            elif ", " in date:
                date = date.replace(",", " ")
                month, day, year = date.split()
                if month in months:
                    month = months.index(month) + 1
                else:
                    raise ValueError
            else:
                raise ValueError
            month, day = int(month), int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except ValueError:
            continue
    print(f"{year}-{month:02d}-{day:02d}")


if __name__ == "__main__":
    main()
