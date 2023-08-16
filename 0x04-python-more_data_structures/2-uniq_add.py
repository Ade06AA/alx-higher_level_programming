#!/usr/bin/python3
def uniq_add(ml=[]):
    ss = list(set(ml))
    """
    nn = []
    for i in range(len(ml)):
        jj = ml.pop()
        nn.append(jj if jj not in ml else 0)
    print(nn)
    """
    total = 0
    for i in ss:
        total += int(i)
    return total
