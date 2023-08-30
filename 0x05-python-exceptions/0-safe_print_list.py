#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="" if i < x - 1 else '\n')
            n += 1
    except:
        pass
    finally:
        return n
