import sys
import heapq as Heap

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

def ParentRoute(parent, n1, n2):
    if n1 not in parent or n2 not in parent:
        return None
    if n1 == n2:
        return []
    route = [n2]
    while n1 != n2:
        n2 = parent[n2]
        if n2 == None: # Not connected
            return None
        route.insert(0, n2)
    return route

def solve(G, n1, case):
    dist, parent = Dijkstra2(G, n1[0])
    route = ParentRoute(parent, n1[0], n1[1])
    if dist[n1[1]] == 0:
        route = [n1[0]]
    routeSTR = ''
    for i in route:
        routeSTR += str(i) + ' '
    print 'Case', str(case) + ': Path =', str(routeSTR[:-1]) + ';', dist[n1[1]], 'second delay'

def pair(L):
    L2 = []
    for i in xrange(len(L)):
        if i % 2 == 0:
            L2.append((L[i], L[i + 1]))
    return L2

def read():
    case = 1
    T = int(sys.stdin.readline())
    while T != 0:
        G = {}
        for n in xrange(1, T + 1):
            adj = map(int, sys.stdin.readline().split())[1:]
            for m, w in pair(adj):
                makeDLinkW(G, n, m, w)
        nd = map(int, sys.stdin.readline().split())
        solve(G, nd, case)
        case += 1
        sys.stdin.readline()
        T = int(sys.stdin.readline())

read()
