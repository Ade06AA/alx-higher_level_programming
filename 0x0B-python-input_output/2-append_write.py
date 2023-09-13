#!/usr/bin/python3
"""
module doc
"""


def append_write(filename='', text=''):
    """
    func doc
    """
    with open(filename, mode='a', encoding='utf-8') as fl:
        n = fl.write(text)
        return n
