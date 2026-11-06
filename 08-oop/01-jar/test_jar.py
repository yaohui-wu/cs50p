import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(99)
    assert jar.capacity == 99
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    jar1.deposit(11)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar2 = Jar()
    jar2.deposit(3)
    assert str(jar2) == "🍪🍪🍪"
    jar2.deposit(7)
    assert str(jar2) == "🍪" * 10


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(9)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
