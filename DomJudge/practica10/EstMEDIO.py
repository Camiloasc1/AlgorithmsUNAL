import random
import sys

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


def med(L):
    return quickSearch(L, len(L) / 2)

def sumW(nums, W):
    check = 0
    for i, w in zip(nums, W):
        check += i * w
    return check

def read():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        E = {}
        n, a = map(int, sys.stdin.readline().split())
        for _ in xrange(n):
            l = sys.stdin.readline().split()
            E[l[0]] = map(int, l[1:a + 1])

        W = map(int, sys.stdin.readline().split())

        for e in E:
            E[e] = sumW(E[e], W)

        E = sorted(E, key = lambda e:E[e])
        print E[n / 2]
        '''
        m = med(E.values())
        for e in E:
            if E[e] == m:
                print e
        '''
read()
