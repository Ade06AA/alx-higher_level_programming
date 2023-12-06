#!/usr/bin/python3
"""
my doc
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        res = requests.get(argv[1]))
        if res.status_code >= 400:
            print("Error code: {}".format(res.status_code))
        else:
            print(res.text)
