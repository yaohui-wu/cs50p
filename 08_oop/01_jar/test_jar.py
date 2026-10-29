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
    # TODO
    raise NotImplementedError


def test_withdraw():
    # TODO
    raise NotImplementedError
