#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    mul = []
    for y in range(len(my_list)):
        if my_list[y] % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)

    return (mul)
