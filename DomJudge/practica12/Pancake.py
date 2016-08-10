import sys

def flip(stack, pos):
    if pos == 0:
        return stack[::-1]
    return stack[:pos] + stack[:pos - 1:-1]

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

def PancakeN_V5(N): # OK-9
    dist = {}

    PN = 0

    root = tuple(range(N))

    queue = []
    queue.append(root)
    dist[root] = 0

    while queue != []:
        n = queue.pop(0)
        nd = dist[n] + 1
        for m in neighbors(n):
            if m not in dist:
                queue.append(m)
                dist[m] = nd
                if nd > PN:
                    PN = nd
    return PN

def main():
    PN = [-1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]
    PNreq = [-1, 1, 1, 1, 3, 20, 2, 35, 455, 5804, 73232, 6, 167]
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

def read():
    PN = [-1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]
    PNreq = [-1, 1, 1, 1, 3, 20, 2, 35, 455, 5804, 73232, 6, 167]

    N = int(sys.stdin.readline())
    while N > 0:
        if N <= 7:
            print PancakeN_V5(N), PNreq[N]
        else:
            print PN[N], PNreq[N]
        N = int(sys.stdin.readline())

read()
