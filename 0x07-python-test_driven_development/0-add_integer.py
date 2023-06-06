#!/usr/bin/python3
"""
This function add 2 integers and float together
"""

def add_integer(a, b=98):
    """
    a & b can only be an integer or floating number
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int (a) + int(b))
