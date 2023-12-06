#!/usr/bin/python3
"""
my doc
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        email = {"email": argv[2]}
        responce = requests.post(argv[1], data=email)
        print(responce.text)
