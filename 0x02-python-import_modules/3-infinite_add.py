#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    overall = 0
    for i in range(len(sys.argv) - 1):
        overall += int(sys.argv[i + 1])
    print("{}".format(overall))
