from plates import is_valid


def main():
    test_start()
    test_length()
    test_numbers()
    test_chars()


def test_start():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False


def test_length():
    assert is_valid("ABC") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False


def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False


def test_chars():
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
