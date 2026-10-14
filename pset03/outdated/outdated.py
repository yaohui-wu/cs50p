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
    year_month_day = None
    while year_month_day is None:
        month_day_year = input("Date: ").strip()
        year_month_day = convert_date(month_day_year)
    # Output format: YYYY-MM-DD
    print(year_month_day)


def convert_date(date):
    try:
        # Format 1: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
        # Format 2: Month DD, YYYY
        else:
            month, day, year = date.split()
            if day.endswith(","):
                day = day.replace(",", "")
            else:
                return None
            month = month.capitalize()
            if month in MONTHS:
                month = MONTHS.index(month) + 1
            else:
                return None
        year, day = int(year), int(day)
        if 1 <= month <= 12 and 1 <= day <= 31:
            year_month_day = f"{year}-{month:02d}-{day:02d}"
            return year_month_day
    except ValueError:
        return None


if __name__ == "__main__":
    main()
