#!/usr/bin/python3
"""
Learning how to assign getter and setter in a rec model
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Property and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Property and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Property and setter for X
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Property and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
