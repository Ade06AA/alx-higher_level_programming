#!/usr/bin/python3
"""
my doc
"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    if len(argv) == 3:
        email = argv[2]
        data = parse.urlencode({'email': email}).encode('ascii')
        req = request.Request(argv[1], data)
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
