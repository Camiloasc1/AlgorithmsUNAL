import sys

def makeDLink(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = True
    if n2 not in G:
        G[n2] = {}

def neighbors(F):
    W = 'W'
    R = 'R'
    B = 'B'

    if F[-1] == W:
        return [[R], [B, R]]
    if F[-1] == R:
        return [[W], [B, W]]

def resCount(n, F):
    count = 0
    for fl in F:
        l = len(fl)
        assert not l < n
        if l == n:
            count += 1
    return count

def check(n, F):
    for fl in F:
        if len(fl) < n:
            return False
    return True

def solve(n1, res):
    W = 'W'
    R = 'R'
    B = 'B'

    F = [[W], [R]]

    for i in xrange(n1 + 1):
#         if i % 2 == 0and i >= 6:
#             res[i] = res[i / 2] ** 2
        if i >= 4:
            res[i] = res[i - 1] + res[i - 2]
            continue
        while not check(i, F):
            F2 = []
            for u in F:
                if len(u) < i:
                    for v in neighbors(u):
                        F2.append(u + v)
                else:
                    F2.append(u)
            F = F2
        res[i] = resCount(i, F)

    return res

def read():
    res = {0:0, 1:2}
    Q = []

    for l in sys.stdin.read().splitlines():
        Q.append(int(l))
#     res = solve(max(Q), res)
    for i in xrange(2, max(Q) + 1):
        res[i] = res[i - 1] + res[i - 2]
    for l in Q:
        print res[l]

read()
