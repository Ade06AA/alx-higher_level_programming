#!/usr/bin/python3
def weight_average(ml=[]):
    if len(ml) == 0:
        return 0
    f1 = 0
    f2 = 0
    for x, y in ml:
        f1 += (x * y)
        f2 += y
    return f1 / f2
