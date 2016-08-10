import sys

def make_link(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    (G[n1])[n2] = 1
    if n2 not in G:
        G[n2] = {}
    (G[n2])[n1] = 1
    return G

def fof(G, a):
    if a not in G:
        return [a]
    check = []
    queue = []
    queue.append(a)
    while queue != []:
        for k in G[queue.pop(0)]:
            if k not in check:
                check.append(k)
                queue.append(k)
    if a not in check:
        check.append(a)
    return check

def solve(G, a, b):
    fofa = fof(G, a)
    fofb = fof(G, b)
    
    if a in fofb:
        return 0
    
    check = len(fofa)
    check *= len(fofb)
    check += len(fofb)
    
    make_link(G, a, b)
    return check

def read():
    n = int(sys.stdin.readline())
    for _ in xrange(n):
        m = int(sys.stdin.readline())
        G = {}
        for _ in xrange(m):
            a, b = sys.stdin.readline().split()
            print solve(G, a, b)
    
read()
