#!/usr/bin/python3
"""Defines a class that checks if is same class method"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of the specified class; otherwise False.

    Args:
        obj (any): The object to check
        a_class (type): The class to match from
    Returns:
        True if obj is an instance of a_class
        Otherwise - False
    """
    return type(obj) is a_class
