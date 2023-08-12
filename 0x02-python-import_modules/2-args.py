#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc - 1, 's' if argc > 2 else ''))
        for i in range(argc - 1):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))
