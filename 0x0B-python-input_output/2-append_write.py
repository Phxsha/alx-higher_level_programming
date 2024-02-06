#!/usr/bin/python3
"""Defines a text file appending function"""


def append_write(filename="", text=""):
    """Function that appends to a file.

    Args:
        filename (any): The file to write on.
        text (string): text to append to the file.
    Return:
        Written file.
    """
    with open(filename, mode='a', encoding='UTF-8') as file:
        return file.write(text)
