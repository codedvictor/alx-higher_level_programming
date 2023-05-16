#!/usr/bin/python3

def no_c(my_string):

    nonec = [ch for ch in my_string if ch != 'C' and ch != 'c']
    return ("".join(nonec))
