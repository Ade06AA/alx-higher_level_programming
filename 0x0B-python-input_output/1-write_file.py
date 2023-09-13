#!/usr/bin/python3
"""module doc
"""


def write_file(filename="", text=""):
    """
    func doc
    """
    with open(filename, mode='w', encoding='utf-8') as file_:
        n = file_.write(text)
        return n
