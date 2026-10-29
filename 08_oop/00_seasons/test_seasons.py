from datetime import date

import pytest

from seasons import parse_date

ERROR_MESSAGE = "Invalid date"
valid_dates = [
    (date.today().isoformat(), date.today()),
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
    "2026-02-29",
    "2026-04-31",
]


def main():
    # TODO
    test_valid_date()
    test_invalid_format()
    test_invalid_date()


@pytest.mark.parametrize("valid_date_str, expected_date", valid_dates)
def test_valid_date(valid_date_str, expected_date):
    assert parse_date(valid_date_str) == expected_date


@pytest.mark.parametrize("invalid_format_str", invalid_formats)
def test_invalid_format(invalid_format_str):
    with pytest.raises(SystemExit) as excinfo: # Exception information
        parse_date(invalid_format_str)
    exit_code = excinfo.value.code
    assert exit_code is not None and exit_code != 0
    assert str(excinfo.value) == ERROR_MESSAGE

@pytest.mark.parametrize("invalid_date_str", invalid_dates)
def test_invalid_date(invalid_date_str):
    with pytest.raises(SystemExit) as excinfo:
        parse_date(invalid_date_str)
    exit_code = excinfo.value.code
    assert exit_code is not None and exit_code != 0
    assert str(excinfo.value) == ERROR_MESSAGE


def test_calculate_minutes():
    # TODO


def test_num_to_words():
    # TODO


if __name__ == "__main__":
    main()
