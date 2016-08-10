import sys

import heapq as Heap

def makeNDLinkW(G, n1, n2, W, add = False):

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

    if add:
        if n1 not in G[n2]:
            G[n2][n1] = 0
        G[n2][n1] += W
    else:
        G[n2][n1] = W

    return G

def FloydWarshall2(G):
    dist = {}
    parent = {}

    for i in G:
        dist[i] = {}
        parent[i] = {}
        for j in G:
            dist[i][j] = float('inf')
            parent[i][j] = None
        dist[i][i] = 0
        for neighbor in G[i]:
            dist[i][neighbor] = G[i][neighbor]
            parent[i][neighbor] = i

    for k in G:
        for i in G:
            for j in G:
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
                    parent[i][j] = parent[k][j]

    return dist, parent

def Dijkstra2(G, root):
    dist = {}
    parent = {}

    for n in G:
        dist[n] = float('inf')
        parent[n] = None
    dist[root] = 0

    h = []
    Heap.heappush(h, (0, root))
    while h != []:
        d, n = Heap.heappop(h)
        for m in G[n]:
            nd = d + G[n][m]
            if nd < dist[m]:
                dist[m] = nd
                parent[m] = n
                Heap.heappush(h, (nd, m))
    return dist, parent

def read():
    N, M, Q = map(int, sys.stdin.readline().split())
    while not (N == 0 and M == 0 and Q == 0):
        G = {}

        for i in xrange(100):
            G[i] = {}

        for _ in xrange(M):
            u, v, w = map(int, sys.stdin.readline().split())
            makeNDLinkW(G, u, v, w)

#         dist, _ = FloydWarshall2(G)
        dist = {}

        for _ in xrange(Q):
            a, b = map(int, sys.stdin.readline().split())
            if a == b:
                print 0
                continue
            if a not in G or b not in G:
                print -1
                continue
            if a not in dist:
                dist[a], _ = Dijkstra2(G, a)
            if dist[a][b] < float('inf'):
                print dist[a][b]
            else:
                print -1

        N, M, Q = map(int, sys.stdin.readline().split())
read()
