#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """ initialization of size of the square.
        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
