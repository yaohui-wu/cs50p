from datetime import date

from seasons import parse_date


def main():
    # TODO


def test_valid_date():
    assert parse_date("2026-01-01") == date(2026, 1, 1)
    assert parse_date("2024-02-29") == date(2024, 2, 29)
    today = date.today()
    assert parse_date(today.isoformat()) == today


def test_invalid_format():
    # TODO


def test_invalid_date():
    # TODO


def test_calculate_minutes():
    # TODO


def test_num_to_words():
    # TODO


if __name__ == "__main__":
    main()
