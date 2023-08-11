#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        for i in range(len(argv) - 1):
            print(f"{i + 1:d}: {argv[i + 1]:s}")