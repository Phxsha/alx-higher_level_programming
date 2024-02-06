#!/usr/bin/python3
"""Defines a class for Student attributes"""


class Student:
    """Class for Student attributes"""

    def __init__(self, first_name, last_name, age):
        """initialization of student attributes.

        Args:
            first_name (str): First name of the Student.
            last_name (str): Last name of the Student.
            age (int): The age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a student.

        If attrs is a list of strings, represents attributes only included in the list.

        Args:
            attrs (list): (Optional) attribute to represent.
        """
        if(type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
