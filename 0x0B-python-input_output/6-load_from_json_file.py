#!/usr/bin/python3
"""
module doc
"""

myjson = __import__("json")
def load_from_json_file(filename):
    """
    larning how to use json in python
    """
    with open(filename, 'r', encoding='utf-8') as jf:
        jc = jf.read(filename)
    return myjson.load(jc)
