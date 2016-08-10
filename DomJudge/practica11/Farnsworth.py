import sys

def makeDLinkW(G, n1, n2, W, add = False):

    if n1 not in G:
        G[n1] = {}

    if add:
        if n2 not in G[n1]:
            G[n1][n2] = 0
        G[n1][n2] += W
    else:
        G[n1][n2] = W

    if n2 not in G:
        G[n2] = {}

    return G

def BellmanFord(G, root):
    Res = 0
    # P = 1

    dist = {}
    for n in G:
        dist[n] = (float('inf'), None)
    dist[root] = (0, None)

    for _ in xrange(len(G) - 1):
        for n in G:
            for m in G[n]:
                nd = dist[n][Res] + G[n][m]
                if nd < dist[m][Res]:
                    dist[m] = (nd, n)

    for n in G:
        for m in G[n]:
            nd = dist[n][Res] + G[n][m]
            assert not nd < dist[m][Res]

    return dist

def HasCycle(G, root):
    try:
        BellmanFord(G, root)
    except AssertionError:
        return True
    return False

def solve(G):
    for root in G:
        if HasCycle(G, root):
            return True
    return False

def read():
    N, B = map(int, sys.stdin.readline().split())
    while N != 0 and B != 0:
        G = {}
        for _ in xrange(B):
            u1, u2, w = map(int, sys.stdin.readline().split())
            makeDLinkW(G, u1, u2, w)
            makeDLinkW(G, u2, u1, -w)
        if solve(G):
            print 'Y'
        else:
            print 'N'
        N, B = map(int, sys.stdin.readline().split())

read()
