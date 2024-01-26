#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents the attributes of the square i.e the size of the sides"""
    def __init__(self, size=0):
        """Initializing the Square"""
        if not isinstance(size, int):
            """Raises: TypeError - If size ! integer"""

            raise TypeError("size must be an integer")

        elif size < 0:
            """Raises: ValueError - If size < 0"""

            raise ValueError("size must be >= 0")

        else:
            self.__size = size
