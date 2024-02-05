#!/usr/bin/python3


class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the given value as an integer."""

        if type(value) is not int:
            """Raise typeerror if name is not an int"""

            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            """Raise a ValueError if name is > 0"""

            raise ValueError(f"{name} must be greater than 0")
