#!/usr/bin/python3
"""Rect class with width, height, area, perim, __str__, & __repr__ methods."""


class Rectangle:
    """The Rectangle class represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        line = str(self.print_symbol) * self.__width
        return '\n'.join(
        [line[i:i + 80] for i in range(0, len(line), 80)
         for _ in range(self.__height)]
        )

    def __repr__(self):
        """Return a formal string representation of the rectangle object."""
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'

    def __del__(self):
        """Print a farewell message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
