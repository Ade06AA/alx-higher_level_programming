#!/usr/bin/python3
"""
module doc
"""

myjson = __import__("json")
def from_json_string(my_str):
    """
    larning how to use json in python
    """
    js = myjson.loads(my_str)
    return js
