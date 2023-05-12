#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    clist = len(sys.argv) - 1
    if clist == 0:
        print("0 arguments.")
    elif clist == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(clist))
    for i in range(clist):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
