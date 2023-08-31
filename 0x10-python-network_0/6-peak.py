#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    list_size = len(list_of_integers)
    if list_size == 1:
        return list_of_integers[0]
    elif list_size == 2:
        return max(list_of_integers)

    mid_int = int(list_size / 2)
    peak = list_of_integers[mid_int]
    if peak > list_of_integers[mid_int - 1] and peak > list_of_integers[mid_int + 1]:
        return peak
    elif peak < list_of_integers[mid_int - 1]:
        return find_peak(list_of_integers[:mid_int])
    else:
        return find_peak(list_of_integers[mid_int + 1:])
