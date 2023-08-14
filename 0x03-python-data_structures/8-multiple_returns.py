#!/usr/bin/python3
def multiple_returns(s):
    return (len(s), None if len(s) == 0 else s[0])
