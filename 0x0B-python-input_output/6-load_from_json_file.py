#!/usr/bin/python3
"""Defines a function that loads an Object in a text file"""
import json


def load_from_json_file(filename):
    """Loads an object to a file using json"""
    with open(filename) as file:
        return json.load(file)

