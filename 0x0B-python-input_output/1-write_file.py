#!/usr/bin/python3
"""Defines a function to wrtie tot a file
   and returns the number of character writen
"""


def write_file(filename="", text=""):
    """writes string to a file"""

    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
