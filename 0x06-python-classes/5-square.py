#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Attributes and methods of the square"""

    def __init__(self, size=0):
        """Initializing the Square"""

        self.size = size

    @property
    def size(self):
        """Get the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""

        if not isinstance(value, int):
            """raise TypeError if val is not an int"""

            raise TypeError("size must be an integer")

        elif value < 0:
            """raise ValueError if value is less than 0"""

            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters"""

        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print("#" * self.__size)
