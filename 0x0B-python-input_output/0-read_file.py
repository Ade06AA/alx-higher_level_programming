#!/usr/bin/python3
"""
module doc
"""


def read_file(filename=""):
    """
    def doc
    """
    with open(filename, mode='r', encoding='utf-8') as fl:
        content = fl.read()
        print("{}".format(content), end="")
