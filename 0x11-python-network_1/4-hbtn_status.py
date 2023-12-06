#!/usr/bin/python3
"""
my doc
"""

import requests

if __name__ == "__main__":
    responce=requests.get("https://alx-intranet.hbtn.io/status")
    html = responce.text
    print("""Body response:$
    - type: {}$
    - content: {}$""".format(type(html), html))
