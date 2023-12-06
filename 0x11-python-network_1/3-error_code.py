#!/usr/bin/python3
"""
my doc
"""
from sys import argv
from urllib import request, error as ER


if __name__ == '__main__':
    if len(argv) == 2:
        try:
            with request.urlopen(argv[1]) as response:
                html = response.read()
                print(html.decode('utf-8'))
        except ER.HTTPError as error:
            print("Error code: {}".format(error.code))
