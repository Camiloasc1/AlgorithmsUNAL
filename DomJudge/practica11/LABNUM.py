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

def neighbors(F):
    x, y = F
    moves = []
    moves.append((x, y + 1))
    moves.append((x, y - 1))
    moves.append((x + 1, y))
    moves.append((x - 1, y))
    return moves

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

def solve(G, n1, m):
    dist, _ = Dijkstra2(G, (0, 0))
    return dist[(n1 - 1, m - 1)] + G[(0, -1)][(0, 0)]

def read():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        m = int(sys.stdin.readline())
        G = {}
        for x in xrange(n):
            cells = map(int, sys.stdin.readline().split())
            for y, c in enumerate(cells):
                for v in neighbors((x, y)):
                    makeDLinkW(G, v, (x, y), c)
        print solve(G, n, m)

read()
