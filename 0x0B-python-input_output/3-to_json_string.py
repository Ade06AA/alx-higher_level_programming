#!/usr/bin/python3
"""
module doc
"""

myjson = __import__("json")
def to_json_string(my_obj):
    """
    larning how to use json in python
    """
    js = myjson.dumps(my_obj)
    return js
