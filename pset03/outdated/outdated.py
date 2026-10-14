MONTHS = [
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


def main():
    year_month_day_list = None
    while year_month_day_list is None:
        date = input("Date: ").strip()
        year_month_day_list = convert_date(date)
    year = year_month_day_list[0]
    month = year_month_day_list[1]
    day = year_month_day_list[2]
    # Output format: YYYY-MM-DD
    date = f"{year}-{month:02d}-{day:02d}"
    print(date)


def convert_date(date):
    try:
        # Format 1: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
        # Format 2: Month DD, YYYY
        elif "," in date:
            date = date.replace(",", " ")
            month, day, year = date.split()
            if month.capitalize() in MONTHS:
                month = MONTHS.index(month) + 1
            else:
                raise ValueError
        else:
            raise ValueError
        year, month, day = int(year), int(month), int(day)
        if 1 <= month <= 12 and 1 <= day <= 31:
            year_month_day_list = [year, month, day]
            return year_month_day_list
    except ValueError:
        return None


if __name__ == "__main__":
    main()
