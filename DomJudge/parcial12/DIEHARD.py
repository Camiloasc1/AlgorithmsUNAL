import  sys

def makeNDLink(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = True
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = True

def BFS2(G, root):
    dist = {}
    parent = {}

    for n in G:
        dist[n] = float('inf')
        parent[n] = None

    dist[root] = 0
    parent[root] = root

    queue = []
    queue.append(root)

    while queue != []:
        n = queue.pop(0)
        for m in G[n]:
            if parent[m] == None:
                dist[m] = dist[n] + 1
                parent[m] = n
                queue.append(m)

    parent[root] = None
    return dist, parent

def ParentRouteLen(parent, n1, n2):
    if n1 not in parent or n2 not in parent:
        return float('inf')
    if n1 == n2:
        return 0
    l = 0
    while n1 != n2:
        n2 = parent[n2]
        if n2 == None: # Not connected
            return float('inf')
        l += 1
    return l

def move(c1, c2):
    CONT = 0
    CAP = 1

    c1, c2 = list(c1), list(c2)
    DISP = c2[CAP] - c2[CONT]
    if DISP >= c1[CONT]: # c1 empty
        c1[CONT], c2[CONT] = 0, c2[CONT] + c1[CONT]
    if DISP < c1[CONT]: # c2 full
        c1[CONT], c2[CONT] = c1[CONT] - DISP, c2[CAP]
    return tuple(c1), tuple(c2)

def drop(c):
    # CONT = 0
    CAP = 1

    return (0, c[CAP])

def neighbors(F):
    c1, c2 = F
    moves = []
    moves.append((drop(c1), c2))
    moves.append((c1, drop(c2)))
    moves.append(move(c1, c2))
    moves.append(move(c2, c1)[::-1])
    return moves

def solve(c1, c2, d1, d2):
    G = {}
    queue = [(c1, c2)]
    while queue != []:
        n1 = queue.pop(0)
        for m in neighbors(n1):
            if m not in G:
                queue.append(m)
            makeNDLink(G, n1, m)
    if (d1, d2) not in G:
        return -1
    else:
        _, parent = BFS2(G, (c1, c2))
        return ParentRouteLen(parent, (c1, c2), (d1, d2))

def read():
    lines = sys.stdin.read().splitlines()
    for l in lines:
        CONT1, CONT2, CAP1, CAP2, D1, D2 = map(int, l.split())
        print solve((CONT1, CAP1), (CONT2, CAP2), (D1, CAP1), (D2, CAP2))

read()
