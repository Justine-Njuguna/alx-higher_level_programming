#!/usr/bin/python3


class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the given value as an integer."""

        if type(value) is not int:
            """TypeError: If the value is not an integer."""

            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            """ValueError: If the value is less than or equal to 0."""

            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with given width and height."""

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description in the specified format."""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Class representing a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance with given size."""

        super().__init__(size, size)
