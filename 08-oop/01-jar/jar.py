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
        if n < 1 or n > self._capacity - self._size:
            raise ValueError("Deposit must be between 1 and remaining slots")
        self._size += n

    def withdraw(self, n: int) -> None:
        if n <= 0 or n > self._size:
            message = "Withdrawal must be between 1 and available size"
            raise ValueError(message)
        self._size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size
