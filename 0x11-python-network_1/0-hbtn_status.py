#!/usr/bin/python3
"""
my doc
"""

import urllib.request as ulibReq


with ulibReq.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("""Body response:$
    - type: {}$
    - content: {}$
    - utf8 content: {}$""".format(type(html), html, html.decode('utf8')))
