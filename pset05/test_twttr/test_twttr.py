from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("HELLO, WORLD!") == "HLL, WRLD!"


if __name__ == "__main__":
    main()
