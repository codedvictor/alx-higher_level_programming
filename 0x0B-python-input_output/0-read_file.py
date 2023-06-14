#!/usr/bin/python3
"""Defines a function to read a text file"""


def read_file(filename=""):
    """Reads a text file and prints it"""

    with open(filename, encoding="utf-8") as fl:
        for rin in fl:
            print(rin, end="")
