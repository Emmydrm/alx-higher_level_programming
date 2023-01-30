#!/usr/bin/python3
"""This module defines a Rectangle class based on 0-rectangle.py"""


class Rectangle:
    """A Rectangle class

    Args:
        width: width of rectangle
        height: height of rectangle

    Raises:
        TypeError: if width or height are not integers
        ValueError: if width or height are less than 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
            return
        if value < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = value

    @property
    def height(self):
        """Height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
            return
        if value < 0:
            raise ValueError("height must be >= 0")
            return
        self.__height = value
