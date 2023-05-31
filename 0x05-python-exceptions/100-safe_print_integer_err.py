#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except BaseException as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return False
    return True
