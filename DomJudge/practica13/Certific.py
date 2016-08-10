import sys

def makeDLink(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = True
    if n2 not in G:
        G[n2] = {}

def solve(G, cert):
    visited = {}
    for i, n1 in enumerate(cert):
        if n1 in visited:
            return False
        else:
            visited[n1] = True
            if cert[(i + 1) % len(cert)] not in G[n1]:
                return False
#     for n1 in G:
#         if n1 not in visited:
#             return False
    if len(G) != len(visited):
            return False
    return True

def read():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        G = {}
        n, m = map(int, sys.stdin.readline().split())
        for i in xrange(n):
            G[i] = {}
        for _ in xrange(m):
            a, b = map(int, sys.stdin.readline().split())
            makeDLink(G, a, b)
        cert = map(int, sys.stdin.readline().split())
        if solve(G, cert):
            print 'si'
        else:
            print 'no'

read()
