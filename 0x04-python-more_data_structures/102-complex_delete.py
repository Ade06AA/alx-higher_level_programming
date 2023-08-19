#!/usr/bin/python3
def complex_delete(a_d, value):
    if a_d is not None:
        v = a_d.values()
        if value in v:
            for i, g in a_d.items():
                if g == value:
                    del a_d[i]
                    complex_delete(a_d, value)
                    break
