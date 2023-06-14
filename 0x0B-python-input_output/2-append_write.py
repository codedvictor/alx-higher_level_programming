#!/usr/bin/python3
"""Defines a function to append a text to a textfile"""


def append_write(filename="", text=""):
    """Append a text to a text fd"""

    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
