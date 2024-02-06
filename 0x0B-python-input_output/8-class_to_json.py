#!/usr/bin/python3
"""Defines a python class to JSON function"""
import json


def class_to_json(obj):
    """Returns class to obj"""
    return json.__dict__
