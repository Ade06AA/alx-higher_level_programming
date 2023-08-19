#!/usr/bin/python3
def print_last_digit(num):
    abd = abs(num)
    print("{:d}".format(abd % 10), end="")
    return abd % 10
