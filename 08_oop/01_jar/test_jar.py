import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity() == 12
    jar = Jar(99)
    assert jar.capacity() == 99


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(7)
    assert str(jar) == "🍪" * 10


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size() == 10
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(9)
    assert jar.size() == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
