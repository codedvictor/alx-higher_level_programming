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

    mid_t = int(list_size / 2)
    pk = list_of_integers[mid_t]
    if pk > list_of_integers[mid_t - 1] and pk > list_of_integers[mid_t + 1]:
        return pk
    elif pk < list_of_integers[mid_t - 1]:
        return find_peak(list_of_integers[:mid_t])
    else:
        return find_peak(list_of_integers[mid_t + 1:])
