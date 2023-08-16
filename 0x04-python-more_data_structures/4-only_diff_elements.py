#!/usr/bin/python3
def only_diff_elements(s1, s2):
    return (s1 | s2) - (s1 & s2)
