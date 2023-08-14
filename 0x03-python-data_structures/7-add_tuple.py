#!/usr/bin/python3

# a function that craete a new two element tuple
# from any two tuple by adding the coresponding first and second
# index of the two tuples
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a, tuple_b
    t = [0, 0]
    for i in range(2):
        t[i] = (a[i] if len(a[i:i + 1]) == 1 else 0)\
                + (b[i] if len(b[i:i + 1]) == 1 else 0)
    return (tuple(t))
