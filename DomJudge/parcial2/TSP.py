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

def solve(G, cert, l):
    visited = {}
    dist = 0
    for n1, n2 in zip(cert[:-1], cert[1:]):
        if n1 in visited:
            return False
        else:
            visited[n1] = True
            if n2 not in G[n1]:
                return False
            dist += G[n1][n2]
#             print (n1, n2), dist
#     for n in G:
#         if n not in visited:
#             return False
    if cert[0] not in G[cert[-1]]:
        return False
    visited[cert[-1]] = True
    if len(G) != len(visited):
        return False
    return dist <= l

def read():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        G = {}
        n, m, l = map(int, sys.stdin.readline().split())
        for i in xrange(n):
            G[i] = {}
        for _ in xrange(m):
            a, b, w = map(int, sys.stdin.readline().split())
            makeDLinkW(G, a, b, w)
        cert = map(int, sys.stdin.readline().split())
        if solve(G, cert, l):
            print 'si'
        else:
            print 'no'

read()
