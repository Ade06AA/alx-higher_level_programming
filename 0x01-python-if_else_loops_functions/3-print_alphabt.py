#!/usr/bin/python3
for ch in range(97, 123):
    print("{:c}".format(0 if (ch == 113 or ch == 101) else ch), end="")
