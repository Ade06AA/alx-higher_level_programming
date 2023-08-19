#!/usr/bin/python3
def uppercase(s):
    for i in s:
        i = ord(i)
        print("{:c}".format(i-32 if i <= 122 and i >= 97 else i), end="")
    print("\n")
