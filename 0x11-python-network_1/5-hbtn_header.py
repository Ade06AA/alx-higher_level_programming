#!/usr/bin/python3
"""
my doc
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        responce = requests.get(argv[1])
        print(responce.headers.get("X-Request-Id"))
