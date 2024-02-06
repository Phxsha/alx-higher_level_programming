#!/usr/bin/python3
"""Defines a text file reading function"""


def read_file(filename=""):
    """Function that reads a file.

    Args:
        filename (any): The file to read.
    Return:
        Nothing.
    """
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
