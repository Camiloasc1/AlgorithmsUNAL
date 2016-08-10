import timeit
import Util.Graph as Graph

def flip(stack, pos):
    if pos == 0:
        return stack[::-1]
    return stack[:pos] + stack[:pos - 1:-1]

def flipSequence(stack, flips):
    for f in flips:
        stack = flip(stack, f)
    return stack

def testFlip():
    S = range(5)
    # print S

    T = flip(S, 0)
    # print T
    assert T == [4, 3, 2, 1, 0]

    T = flip(S, 1)
    assert T == [0, 4, 3, 2, 1]

    T = flip(S, 2)
    assert T == [0, 1, 4, 3, 2]

    T = flip(S, 3)
    assert T == [0, 1, 2, 4, 3]

    T = flip(S, 4)
    assert T == [0, 1, 2, 3, 4]

    T = flip(S, 5)
    assert T == [0, 1, 2, 3, 4]

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def testFlipTime():
    n = 5
    S = range(n)
    testFlip()
    wrapped = wrapper(flip, S, n / 2)
    print timeit.timeit(wrapped)
    wrapped = wrapper(flipSequence, S, range(n))
    print timeit.timeit(wrapped)

def PancakeGraph(N, weighted = True, W = None):
    P = {}
    S = tuple(range(N))
    queue = [S]
    while queue != []:
        c = list(queue.pop(0))
        cT = tuple(c)
        if cT not in P:
            P[cT] = {}
        for i in xrange(N - 1):
            c2T = tuple(flip(c, i))
            if c2T not in P[cT]:
                queue.append(c2T)
                if weighted:
                    if W == None:
                        Graph.makeNDLinkW(P, cT, c2T, i)
                    else:
                        Graph.makeNDLinkW(P, cT, c2T, W)
                else:
                    Graph.makeNDLink(P, cT, c2T)

def PancakeN1(G): # OK-5
    PN = 0
    dist, _ = Graph.FloydWarshall2(G)
    for i in dist:
        for j in dist[i]:
            if dist[i][j] > PN:
                PN = dist[i][j]
    return PN

def PancakeN2(G): # OK-8
    PN = 0
    dist, _ = Graph.Dijkstra2(G, G.keys()[0])
    for i in dist:
            if dist[i] > PN:
                PN = dist[i]
    return PN

def PancakeN3(G): # OK-8
    PN = 0
    dist, _ = Graph.BFS2(G, G.keys()[0])
    for i in dist:
            if dist[i] > PN:
                PN = dist[i]
    return PN

def neighbors(F, lim = None):
    neighbors = []
    l = 0
    if lim == None:
        l = len(F) - 1
    else:
        l = lim
    for i in xrange(l):
        neighbors.append(tuple(flip(F, i)))
    return neighbors

def PancakeN4(N): # OK-9
    dist = {}

    PN = 0

    root = tuple(range(N))

    dist[root] = 0

    queue = []
    queue.append(root)
    G = {root:{}}

    while queue != []:
        n = queue.pop(0)
        for m in neighbors(n):
            if m not in G:
                queue.append(m)
                nd = dist[n] + 1
                dist[m] = nd
                if nd > PN:
                    PN = nd
                    print m, PN
            Graph.makeNDLink(G, n, m)
    return PN

def PancakeN_V5(N): # OK-9
    dist = {}

    PN = 0

    root = tuple(range(N))

    queue = []
    queue.append(root)
    dist[root] = 0
    print root, 0

    while queue != []:
        n = queue.pop(0)
        nd = dist[n] + 1
        for m in neighbors(n):
            if m not in dist:
                queue.append(m)
                dist[m] = nd
                if nd > PN:
                    PN = nd
                    print m, PN
    return PN

def main():
    PN = [-1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]
    N = 7
    # testFlipTime()

    # G = PancakeGraph(N, True, 1)
    # P = PancakeN1(G)
    # P = PancakeN2(G)

    # G = PancakeGraph(N, False)
    # P = PancakeN3(G)

    # P = PancakeN4(N)
    P = PancakeN_V5(N)

    print 'P[' + str(N) + '] =', PN[N], '->', P
    assert P == PN[N]
main()
