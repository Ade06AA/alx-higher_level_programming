#!/usr/bin/python3
def divisible_by_2(m_l=[]):
    if len(m_l) == 0:
        return None
    n_l = m_l[:]
    for i in range(len(m_l)):
        if m_l[i] % 2 == 0:
            n_l[i] = True
        else:
            n_l[i] = False
    return n_l
