import pytest

from working import convert


def main():
    test_valid()
    test_invalid_time()
    test_invalid_format()


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 2 AM")
    with pytest.raises(ValueError):
        convert("1 PM to 21:59 AM")
    with pytest.raises(ValueError):
        convert("24 AM to 11:59 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()
