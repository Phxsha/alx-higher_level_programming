#!/usr/bin/python3
""" Defines a Rectangle class"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter retrieving the width attribute of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter that modifies the attribute for the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter retrieving the height attribute of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter that modifies the attribute for the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
