#!/usr/bin/python3
"""function that write from same class or inherit"""


def inherits_from(obj, a_class):
    """function to check instance"""
    if type(obj) is a_class:
        return False
    else:
        return True
