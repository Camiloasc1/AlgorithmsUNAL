import sys

def make_link(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = 1
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = 1
    return G

def solve(G, v):
    if v not in G:
        return
    vecinos = G[v].keys()
    if len(vecinos) == 0:
        return
    Nv = 0
    for k in vecinos:
        for l in vecinos:
            if l in G[k]:
                Nv += 0.5
    Kv = len(vecinos)
    Nv = int(Nv)
    print Nv, Kv
    return

def read():
    for _ in xrange(int(sys.stdin.readline())):
        G = {}
        line = sys.stdin.readline()
        n, m, v = map(int, line.split())
        for _ in xrange(m):
            line = sys.stdin.readline()
            a, b = map(int, line.split())
            make_link(G, a, b)
        solve(G, v)
    return

read()
