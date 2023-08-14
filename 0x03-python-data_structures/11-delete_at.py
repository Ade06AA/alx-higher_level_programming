#!/usr/bin/python3
def delete_at(m_l=[], idx=0):
    if idx > len(m_l):
        return m_l
    del(m_l[idx])
    return m_l
