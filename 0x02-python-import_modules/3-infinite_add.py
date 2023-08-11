#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    # remove the first element in the list
    argv.pop(0)
    # or
    # use unpacking method
    # _, *argv = argv
    # this way the fist value will be asigne to _
    sum = 0
    for i in argv:
        i = int(i)
        sum += i
    print(f"{sum:d}")
