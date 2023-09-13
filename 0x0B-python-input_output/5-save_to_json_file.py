#!/usr/bin/python3
"""
module doc
"""
myjson = __import__("json")


def save_to_json_file(my_obj, filename):
    """
    larning how to use json in python
    """
    js = myjson.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as jf:
        jf.write(js)
