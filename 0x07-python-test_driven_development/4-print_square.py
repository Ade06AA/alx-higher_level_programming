#!/usr/bin/python3
"""
module doc
"""


def print_square(size):
    """
    func that prints a square with the character #.
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
