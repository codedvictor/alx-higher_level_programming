#!/usr/bin/python3
"""Defines a function to create an object
   from a JSON file
"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as fl:
        return json.load(fl)
