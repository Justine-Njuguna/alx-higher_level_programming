#!/usr/bin/python3
"""
Module for the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Sqyare class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigning arguments to attributes
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
