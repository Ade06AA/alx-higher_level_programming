#!/usr/bin/python3
def delete_at(m_l=[], idx=0):
    if int(idx) < 0 or int(idx) > (len(m_l) - 1):
        return m_l
    del m_l[int(idx)]
    return m_l
