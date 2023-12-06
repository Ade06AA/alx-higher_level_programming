#!/usr/bin/python3
"""
my doc
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2 or len(argv) == 3:
        if len(argv) == 2:
            val = {"q": ''}
        else:
            val = {"q": argv[2]}
        responce = requests.post(argv[1], data=val)
        try:
            res = responce.json()
            if res:
                print("[{}] {}".format(res.get("id"), res.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a va1id JSON")
