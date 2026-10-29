"""
CS50P Problem Set 8: Cookie Jar

Implement a cookie jar class to store cookies.
"""


class Jar:
    def __init__(self, capacity: int = 12) -> None:
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self) -> str:
        return "🍪" * self._size

    def deposit(self, n: int) -> None:
        # TODO
        raise NotImplementedError

    def withdraw(self, n: int) -> None:
        # TODO
        raise NotImplementedError

    @property
    def capacity(self) -> int:
        # TODO
        raise NotImplementedError

    @property
    def size(self) -> int:
        # TODO
        raise NotImplementedError
