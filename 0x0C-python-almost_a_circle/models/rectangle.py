#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gettr for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        return self.__width = value

    @property
    def height(self):
        """Gettr for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        return self.__height = value

    @property
    def x(self):
        """Gettr for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        return self.__x = value

    @property
    def y(self):
        """Gettr for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        return self.__y = value
