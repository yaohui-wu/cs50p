from datetime import date

import pytest

from seasons import parse_date


def main():
    # TODO
    test_valid_date()
    test_invalid_format()


def test_valid_date():
    assert parse_date("2026-01-01") == date(2026, 1, 1)
    assert parse_date("2024-02-29") == date(2024, 2, 29)
    today = date.today()
    assert parse_date(today.isoformat()) == today


def test_invalid_format():
    with pytest.raises(ValueError):
        parse_date("1/1/2026")
    with pytest.raises(ValueError):
        parse_date("January 1, 1999")
    with pytest.raises(ValueError):
        parse_date("10-31-2026")


def test_invalid_date():
    # TODO


def test_calculate_minutes():
    # TODO


def test_num_to_words():
    # TODO


if __name__ == "__main__":
    main()
