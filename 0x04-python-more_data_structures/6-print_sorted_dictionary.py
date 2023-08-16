#!/usr/bin/python3
def print_sorted_dictionary(d):
    k = list(d.keys())
    k.sort()
    for i in k:
        print("{:s}: {}".format(i, d[i]))
