#!/usr/bin/python3
"""Define a clas from a class from a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or if obj is an instance of a class that inherited from, the specified class; otherwise False.

    Args:
        obj (any): the object.
        a_class (type): the class to check from.

    Returns:
        if is instance - True
        otherwise - False
    """
    if isinstance(obj,a_class):
        return True
    return False
