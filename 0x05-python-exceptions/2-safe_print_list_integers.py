#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_print += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return int_print
