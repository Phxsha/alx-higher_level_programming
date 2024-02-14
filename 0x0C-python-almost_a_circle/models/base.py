#!/usr/bin/python3
"""Defines a base Class for the id used in the project"""
import json
import csv
import turtle


class Base:
    """Base Class for managing id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON sterilization of a list of objects to a file

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

