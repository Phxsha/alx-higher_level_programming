#!/usr/bin/python3
"""Define a clas from a class from a class"""


def is_kind_of_class(obj, a_class):
    """Class and inherited class function.

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
