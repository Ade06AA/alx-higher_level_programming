#!/usr/bin/python3
"""
my doc
"""

import urllib.request as ulibReq
from sys import argv

with ulibReq.urlopen(argv[1]) as response:
    id = response.headers['X-Request-Id']
    print(id)
