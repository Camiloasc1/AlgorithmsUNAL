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

def BellmanFord2(G, root):
    dist = {}
    parent = {}

    for n in G:
        dist[n] = float('inf')
        parent[n] = None
    dist[root] = 0

    for _ in xrange(len(G) - 1):
        for n in G:
            for m in G[n]:
                nd = dist[n] + G[n][m]
                if nd < dist[m]:
                    dist[m] = nd
                    parent[m] = n

    for n in G:
        for m in G[n]:
            nd = dist[n] + G[n][m]
            assert not nd < dist[m]

    return dist, parent

def BellmanFord3(N, E, root):
    dist = {}
    parent = {}

    for n in N:
        dist[n] = float('inf')
        parent[n] = None
    dist[root] = 0

    for _ in xrange(len(N) - 1):
        for n, m in E:
            nd = dist[n] - 1
            if nd < dist[m]:
                dist[m] = nd
                parent[m] = n

    for n, m in E:
        nd = dist[n] - 1
        assert not nd < dist[m]

    return dist, parent

def sol(G):
    visited = {}
    dist = {}
    parent = {}
    pos = {}
    check = []
    for u in G:
        visited[u] = False
        parent[u] = None
    d = 0
    for u in G:
        if not visited[u]:
            d = visit(G, u, d, visited, dist, parent, pos, check)
    # print check
    # return len(check)
    # print d, visited, dist, parent, pos, check
    l = 0
    start = []
    for n in G:
        if G[n] == {}:
            start.append(n)
            l = max(l, dist[n])
    return l

def visit(G, u, d, visited, dist, parent, pos, check):
    visited[u] = True
    d += 1
    dist[u] = d
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            d = visit(G, v, d, visited, dist, parent, pos, check)
    d += 1
    pos[u] = d
    check.append(u)
    return d

def solve(G, N, E):
    m = 0
    for root in G:
        # try:
            dist, _ = BellmanFord3(N, E, root)
            for i in dist:
                if dist[i] < m:
                    m = dist[i]
        # except AssertionError:
            pass
    return -m

def read():
    for line in sys.stdin.readlines():
        nodes = map(int, line.strip().split())
        G = {}
        E = []
        N = []
        for i in xrange(0, len(nodes), 2):
            if nodes[i] == 0 or nodes[i + 1] == 0:
                break
            makeDLinkW(G, nodes[i], nodes[i + 1], -1)
            E.append((nodes[i], nodes[i + 1]))
            N.extend([nodes[i], nodes[i + 1]])

        # print solve(G, list(set(N)), E)
        print max([sol(G), solve(G, list(set(N)), E)])
read()
