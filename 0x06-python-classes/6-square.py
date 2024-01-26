#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Attributes of the square and its methods"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""

        if not isinstance(value, int):
            """Raises TypeError: If value is not an integer"""

            raise TypeError("size must be an integer")

        elif value < 0:
            """Raises ValueError: If value is less than 0"""

            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""

        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            """Raise TypeError: If value !tuple of 2 positive integers"""

            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """calculates the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' chars and space based on position"""

        if self.__size == 0:
            print()

        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
