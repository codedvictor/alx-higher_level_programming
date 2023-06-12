#!/usr/bin/python3
"""function that write from same class or inherit"""


def is_kind_of_class(obj, a_class):
    """function to check instance"""
    if isinstance (obj, a_class):
        return True
    else:
        return False
