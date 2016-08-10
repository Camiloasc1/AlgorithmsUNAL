import sys

def make_link(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = 1
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = 1
    return G

def solve(G):
    vecinos = {}
    color = {}
    for k in G:
        vecinos[k] = G[k].keys()
        color[k] = True
    
    for k in vecinos:
        for l in vecinos[k]:
            color[l] = not color[k]

    for k in vecinos:
        for l in vecinos[k]:
            if color[k] == color[l]:
                return False
    return True

def read():
    n = int(sys.stdin.readline())
    while n != 0 :
        G = {}
        m = int(sys.stdin.readline())
        for _ in xrange(m):
            line = sys.stdin.readline()
            a, b = map(int, line.split())
            make_link(G, a, b)
        if solve(G):
            print 'BICOLORABLE.'
        else:
            print 'NOT BICOLORABLE.'
        n = int(sys.stdin.readline())
    return

read()
