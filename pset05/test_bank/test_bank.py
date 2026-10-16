from bank import value


def main():
    test_hello()
    test_h()
    test_default()


def test_hello():
    assert value("HELLO") == "$0"


def test_h():
    assert value("hi") == "20"


def test_default():
    assert value("What's up") == "$100"


if __name__ == "__main__":
    main()
