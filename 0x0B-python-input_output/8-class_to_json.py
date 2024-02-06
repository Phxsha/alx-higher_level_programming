#!/usr/bin/python3
"""Defines a python class to JSON function"""


def class_to_json(obj):
    """Returns class to obj"""
    return obj.__dict__
