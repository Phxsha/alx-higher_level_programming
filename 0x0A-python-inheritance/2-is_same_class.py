#!/usr/bin/python3
"""Defines a class that checks if is same class method."""


def is_same_class(obj, a_class):
    """Checks True if obj is exactly an instance of the specified class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match from.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
