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
        try:
            date = input("Date: ")
            month, day, year = date.split("/")
        except ValueError:
            month_day, year = date.split(", ")
            month, day = month_day.split()
            month = months.index(month) + 1
        month, day = int(month), int(day)
        if 1 <= month < 12 and 1 <= day <= 31:
            break
    print(f"{year}-{month:02d}-{day:02d}")


if __name__ == "__main__":
    main()
