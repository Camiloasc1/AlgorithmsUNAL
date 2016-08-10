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

def solve(G, n, m):
    res = -1
    for n1 in [(i, -1) for i in xrange(n)]:
        dist, _ = Dijkstra2(G, n1)
#         print n1, G[n1]
        for n2 in [(i, m - 1) for i in xrange(n)]:
#             d = dist[n2] + G[(n1[0], -1)][n1]
            d = dist[n2]
#             print n2, d
            if d < res or res == -1:
                res = d
    return res

def solve2(G, n, m):
    res = float('inf')
    inN, outN = None, None
    minin = float('inf')
    minout = float('inf')
    for nd in [(i, 0) for i in xrange(n)]:
        d = G[(nd[0], -1)][nd]
        if d < minin:
            minin = d
            inN = nd
    for nd in [(i, m) for i in xrange(n)]:
        d = G[(nd[0], m - 1)][nd]
        if d < minout:
            minout = d
            outN = nd
    print inN, outN
    dist, _ = Dijkstra2(G, inN)
    return dist[outN]

def solve3(G, n, m):
    inN = None
    minin = float('inf')
    for i in xrange(n):
        d = G[(i, -1)][(i, 0)]
        if d < minin:
            minin = d
            inN = (i, 0)
    dist, _ = Dijkstra2(G, inN)
    res = float('inf')
    for i in xrange(n):
        d = dist[(i, m)]
        if d < res:
            res = d
    return res

def solve4(G, n, m):
    res = float('inf')
    for n1 in [(i, -1) for i in xrange(n)]:
        dist, _ = Dijkstra2(G, n1)
#         print n1, G[n1]
        for n2 in [(i, m - 1) for i in xrange(n)]:
#             d = dist[n2] + G[(n1[0], -1)][n1]
            d = dist[n2]
#             print n2, d
            if d < res or res == -1:
                res = d
    return res

def read2():
    T = int(sys.stdin.readline())
    for case in xrange(T):
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            print 'Case ' + str(case + 1) + ':', 0
            continue
        G = {}
        for x in xrange(n):
            cells = map(int, sys.stdin.readline().split())
            for y, c in enumerate(cells):
                for v in neighbors((x, y)):
                    makeNDLinkW(G, v, (x, y), c)
        print 'Case ' + str(case + 1) + ':', solve3(G, n, m)

def read():
    T = int(sys.stdin.readline())
    for case in xrange(T):
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            print 'Case ' + str(case + 1) + ':', 0
            continue
        G = {}
        for x in xrange(n):
            G[x] = list(map(int, sys.stdin.readline().split()))
        print 'Case ' + str(case + 1) + ':', solve4(G, n, m)

read()
