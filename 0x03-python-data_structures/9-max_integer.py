#!/usr/bin/python3
def max_integer(m_l=[]):
    if len(m_l) == 0:
        return None
    x = m_l[0]
    for i in m_l:
        x = i if i > x else x
    return x
