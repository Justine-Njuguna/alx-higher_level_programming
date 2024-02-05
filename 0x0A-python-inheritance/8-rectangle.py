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
