#!/usr/bin/python3
"""Defines a text file writing function"""


def read_file(filename="", text=""):
    """Function that writes to a file.

    Args:
        filename (any): The file to write on.
        text (string): text to write to the file.
    Return:
        Written file.
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        return file.write(text)
