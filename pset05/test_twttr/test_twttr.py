from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


if __name__ == "__main__":
    main()
