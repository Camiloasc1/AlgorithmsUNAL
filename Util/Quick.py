import random

def split(L):
    p = random.choice(L)
    l, r = [], []
    m = 0
    for e in L:
        if e < p:
            l.append(e)
        elif e > p:
            r.append(e)
        else:
            m += 1

    return l, [p] * m, r

def quickSort(L):
    if len(L) <= 1:
        return L
    l, m, r = split(L)
    return quickSort(l) + m + quickSort(r)

def quickSearch(L, pos):
    if len(L) <= 1:
        return L
    l, m, r = split(L)
    if len(l) > pos: # In l
        return quickSearch(l, pos)
    elif len(l) + len(m) > pos: # In m
        return m[0]
    else: # In r
        return quickSearch(r, pos - (len(l) + len(m)))
