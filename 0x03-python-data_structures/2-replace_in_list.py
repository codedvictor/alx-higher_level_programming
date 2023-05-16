#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx >= 0 & idx < (len(my_list)):
        my_list[idx] = element
    else:
        my_list[idx] = my_list[idx]
    return (my_list)
