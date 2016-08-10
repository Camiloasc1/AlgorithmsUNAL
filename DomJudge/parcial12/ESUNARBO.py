import sys

def makeDLink(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = True
    if n2 not in G:
        G[n2] = {}

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

def HasCycle(G):
    try:
        BellmanFord(G, G.keys()[0])
    except AssertionError:
        return True
    return False

def solve(G):
    root = None
    for n1 in G:
        while len(G[n1]) != 0: # Has no parent
            if len(G[n1]) > 1: # More than one parent
                return False
            else:
                n1 = G[n1].keys()[0]
        else:
            if root == None:
                root = n1
            if n1 != root:
                return False
    return True

def read():
    for line in sys.stdin.readlines():
        nodes = map(int, line.strip().split())
        G1 = {}
        G2 = {}
        for i in xrange(0, len(nodes), 2):
            if nodes[i] == 0:
                break
            makeDLinkW(G1, nodes[i], nodes[i + 1], -1)
            makeDLink(G2, nodes[i + 1], nodes[i])

        if HasCycle(G1):
            print "it is not a tree."
            continue
        if solve(G2):
            print "it is a tree."
        else:
            print "it is not a tree."
read()
