#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    maxint = my_list[0]
    for y in range(len(my_list)):
        if my_list[y] > maxint:
            maxint = my_list[y]

    return (maxint)
