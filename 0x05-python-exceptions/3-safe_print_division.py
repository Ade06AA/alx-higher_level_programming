#!/usr/bin/python3
def safe_print_division(a, b):
    s = None
    try:
        s = a / b
    except:
        pass
    finally:
        print("Inside result: {}".format(s))
        return s
