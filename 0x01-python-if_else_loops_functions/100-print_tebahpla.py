#!/usr/bin/python3
for ch range (122,98,-1):
    print("{:c}".format(ch if ch % 2 == 0 else ch - 32), end = "")
