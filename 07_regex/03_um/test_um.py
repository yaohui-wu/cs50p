from um import count


def test_valid():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1


def test_invalid():
    assert count("yum") == 0
    assert count("yummy") == 0


def test_mixed():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
