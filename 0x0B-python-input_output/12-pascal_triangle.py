#!/usr/bin/python3
"""Defines a function to returns a list of lists
   of integers representing the Pascal's trinagle of n
"""


def pascal_triangle(n):
    """Returns the Pascal's triangle"""
    if n <= 0:
        return []

    trg = [[1]]
    for x in range(x, n):
        row = [1]
        for y in range(1, x):
            row.append(trg[x - 1][y - 1] + trg[x - 1][y])
        row.append(1)
        trg.append(row)

    return trg
