import math
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
            nd = float(max(float(d), float(G[n][m])))
#             nd = d + G[n][m]
            if nd < dist[m]:
                dist[m] = nd
                parent[m] = n
                Heap.heappush(h, (nd, m))
    return dist, parent

def read():
    T = 1
    N, R, C = map(int, sys.stdin.readline().split())
    while not (N == 0 and R == 0 and C == 0):
#         if T > 1:
        print 'Scenario #' + str(T)
        T += 1
        G = {}

        for _ in xrange(R):
            u, v, w = sys.stdin.readline().split()
            w = float(w)
            if w == 0:
                makeNDLinkW(G, u, v, float(0))
            else:
                makeNDLinkW(G, u, v, float(1) / w)

        dist = {}

        for _ in xrange(C):
            a, b = sys.stdin.readline().split()
#             if a == b:
#                 print 0, 'tons'
#                 continue
            if a not in G or b not in G:
                print -1, 'tons',
                continue
            if a not in dist:
                dist[a], _ = Dijkstra2(G, a)
            if float(dist[a][b]) < float('inf'):
                if float(dist[a][b]) == float(0):
                    print 0, 'tons',
                else:
#                     print int(math.ceil(float(1) / float(dist[a][b]))), 'tons',
                    print int(math.floor(float(1) / float(dist[a][b]))), 'tons',
            else:
                print -1, 'tons',
            print
            print
        N, R, C = map(int, sys.stdin.readline().split()) # here
read()
