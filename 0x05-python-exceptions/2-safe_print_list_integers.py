#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="" if i < x - 1 else '\n')
            n += 1
        except Exception as er:
            if type(er) == IndexError:
                raise
            pass
    return n
