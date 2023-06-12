#!/usr/bin/python3
"""funciton that print all available attributes"""


def lookup(obj):
    """return the available attributes"""
    return (dir(obj))
