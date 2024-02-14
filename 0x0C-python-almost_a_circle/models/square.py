#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a square

        Args:
            size (int): The size of the new square
            x (int): x coordinate of the square
            y (int): y coordinate of the new square
            id (int): The identity of the new square
        """
        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Get/set the size of Square"""
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def __str__(self):
            """Return the print() and str() representation of a Square."""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
