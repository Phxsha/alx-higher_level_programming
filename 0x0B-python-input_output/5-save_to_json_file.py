#!/usr/bin/python3
"""Defines a function that writes an Object in a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using json"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
