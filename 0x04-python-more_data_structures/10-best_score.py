#!/usr/bin/python3
def best_score(d):
    if d is None:
        return None
    bk, oldj = list(d.items())[0]
    for i, j in d.items():
        bk = i if int(j) > oldj else bk
        oldj = int(j)
    return bk
