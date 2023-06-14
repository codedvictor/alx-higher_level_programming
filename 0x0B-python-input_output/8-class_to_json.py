#!/usr/bin/python3
"""Defines a function that returns the dictionary description
   with simple data structure for a JSON
"""


def class_to_json(obj):
    """Returns the dictionary description"""
    desDict = {}
    if hasattr(obj, '__dict__'):
        desDict = obj.__dict__
    return desDict
