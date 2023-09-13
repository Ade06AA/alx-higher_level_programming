#!/usr/bin/python3
"""
module doc
"""
import sys

sf = __import__("5-save_to_json_file").save_to_json_file
lf = __import__("6-load_from_json_file").load_from_json_file
for i in sys.argv[1:]:
    hh = []
    try:
        hh = lf("add_item.json")
    except Exception:
        pass
    sf(hh + [i], "add_item.json")
