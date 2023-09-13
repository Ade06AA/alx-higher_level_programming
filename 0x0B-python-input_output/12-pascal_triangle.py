#!/usr/bin/python3
"""
module doc
"""


def pascal_triangle(n):
    """
    func doc
    """
    ll = []
    if n < 1:
        return ll
    for i in range(1, n+1):
        n = []
        num = 1
        for j in range(1, i+1):
            n.append(num)
            num = num * (i - j) // j
        ll.append(n)
    return ll
