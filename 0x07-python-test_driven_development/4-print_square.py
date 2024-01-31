#!/usr/bin/python3


def print_square(size):
    """Prints a square with the character #"""

    if not isinstance(size, int):
        """Raises TypeError if size is not an integer"""

        raise TypeError("size must be an integer")

    if size <= 0 or (isinstance(size, float) and size < 0):
        """Raises a ValueError if size is not >= 0"""

        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
