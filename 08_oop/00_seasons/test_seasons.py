from datetime import date

import pytest

from seasons import calculate_minutes, num_to_words, parse_date

ERROR_MESSAGE = "Invalid date"
today = date.today()
valid_dates = [
    (today.isoformat(), today),
    ("2026-01-01", date(2026, 1, 1)),
    ("2026-02-28", date(2026, 2, 28)),
    ("2024-06-30", date(2024, 6, 30)),
    ("2024-12-31", date(2024, 12, 31)),
    ("2024-02-29", date(2024, 2, 29)),
]
invalid_formats = [
    "1/1/2026",
    "January 1, 1999",
    "10-31-2026",
    "2000-01-01abc",
    "2046-Jan-01",
    "",
]
invalid_dates = [
    "2026-00-01",
    "2026-13-01",
    "2026-01-00",
    "2100-02-29",
    "2026-03-32",
    "2026-04-31",
]


@pytest.mark.parametrize("valid_date_str, expected_date", valid_dates)
def test_valid_date(valid_date_str, expected_date):
    assert parse_date(valid_date_str) == expected_date


@pytest.mark.parametrize("invalid_format_str", invalid_formats)
def test_invalid_format(invalid_format_str):
    with pytest.raises(SystemExit) as excinfo:  # Exception information
        parse_date(invalid_format_str)
    assert excinfo.value.code == ERROR_MESSAGE


@pytest.mark.parametrize("invalid_date_str", invalid_dates)
def test_invalid_date(invalid_date_str):
    with pytest.raises(SystemExit) as excinfo:
        parse_date(invalid_date_str)
    assert excinfo.value.code == ERROR_MESSAGE


def test_calculate_minutes():
    end_date = date(2026, 1, 1)
    start_date = date(2025, 1, 1)
    leap_year_date = date(2024, 1, 1)  # Leap year
    assert calculate_minutes(start_date, end_date) == 525_600
    assert calculate_minutes(leap_year_date, end_date) == 1_052_640
    assert calculate_minutes(end_date, end_date) == 0  # Same day


def test_num_to_words():
    word1 = "five hundred twenty-five thousand, six hundred"
    assert num_to_words(525_600) == word1
    word2 = "one million, fifty-two thousand, six hundred forty"
    assert num_to_words(1_052_640) == word2
