from twttr import shorten


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("HELLO, WORLD!") == "HLL, WRLD!"
