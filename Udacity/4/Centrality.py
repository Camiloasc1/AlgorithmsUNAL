import random
import sys
import thread
import threading
import time

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

def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = w
    return G

def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values())) / len(distance_from_start)

def centralityThread(G, N, C, lock):
    lock.acquire()
    C = {}
    for n in N:
        C[n] = centrality(G, n)
    lock.release()

def centralityCalc(G, nodes, tc):
    N = []
    C = []
    lock = []
    for i in xrange(tc):
        N.append([])
        C.append({})
        lock.append(threading.Lock())

    cr = 0
    for n in nodes:
        N[cr].append(n)
        cr = (cr + 1) % tc

    for i in xrange(tc):
        thread.start_new_thread(centralityThread, (G, N[i], C[i], lock[i]))

    time.sleep(15)
    for i in xrange(tc):
        lock[i].acquire()
    for i in xrange(tc):
        lock[i].release()

    R = {}
    for i in xrange(tc):
        for a in C[i]:
            R[a] = C[a]
    return R

def read():
    films = {}
    actors = []
    lines = sys.stdin.readlines()

    print "Reading...",

    for line in lines:
        a, f, _ = line.strip().split('\t')
        if a not in actors:
            actors.append(a)
        make_link(films, a, f, True)
    '''
    for f in films:
        for a in f:
            for a2 in f:
                if a != a2:
                    make_link2(actors, a, a2, True)
    '''

    print "OK"
    print "Centrality...",

    # C = centralityCalc(films, actors, 8);

    C = {}
    for n in actors:
        C[n] = centrality(films, n)


    L = C.values()

    print "OK"
    print "Search..."

    check = quickSearch(L, 19)
    print "Res[19]:", check
    for a in C:
        if C[a] == check:
            print "Actor:", a, C[a]

    check = quickSearch(L, 20)
    print "Res[20]:", check
    for a in C:
        if C[a] == check:
            print "Actor:", a, C[a]
    print "Finished"

read()
