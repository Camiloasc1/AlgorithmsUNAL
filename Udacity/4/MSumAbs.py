#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
#
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


def minimize_absolute(L):
    return quickSearch(L, len(L) / 2)
