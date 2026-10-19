import random

import pytest
from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")
        convert("-3/4")
        convert("5/4")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    for _ in range(10):
        random_int = random.randint(2, 98)
        assert gauge(random_int) == f"{random_int}%"


if __name__ == "__main__":
    main()
