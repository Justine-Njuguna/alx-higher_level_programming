#!/usr/bin/python3


class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raise an exception if area is not implemented"""

        raise Exception("area() is not implemented")
