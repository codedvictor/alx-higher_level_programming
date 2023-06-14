#!/usr/bin/python3
"""Defines a function to insert a line after a line
   containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file after each
       line containing a specif string
    """
    listing_line = []
    with open(filename, "r", encoding="utf-8") as fl:
        for line in fl:
            listing_line.append(line)
            if line.find(search_string) != -1:
                listing_line.append(new_string)

    with open(filename, "w", encoding="utf-8") as fl:
        fl.writelines(listing_line)
