#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Attributes of the square e.g their methods"""

    def __init__(self, size=0):
        """Initializing the Square"""

        if not isinstance(size, int):
            """Raising a TypeError if size is not an int"""

            raise TypeError("size must be an integer")

        elif size < 0:
            """Raising a ValueError if size < 0"""

            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Calculates the area of the Square and returns int area of the sq"""

        return self.__size ** 2
