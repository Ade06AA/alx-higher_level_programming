#!/usr/bin/python3
"""
my doc
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
        url = "https://api.github.com/user"
        responce = requests.get(url, auth=auth)
        try:
            res = responce.json()
            print(res.get("id"))
        except ValueError:
            print("Not a va1id JSON")
