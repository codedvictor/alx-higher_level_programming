#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for z in range(len(matrix[y])):
            print("{:d}".format(matrix[y][z]), end="")
            if z != (len(matrix[y]) - 1):
                print(" ", end="")

        print("")
