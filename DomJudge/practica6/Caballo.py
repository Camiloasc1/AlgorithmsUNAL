import sys

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digits = [i for i in xrange(1, 9)]

def make_link(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = 1
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = 1
    return G

def getMoves(c):
    range = [i for i in xrange(1, 8)]
    c = (alpha.index(c[0]), c[1])
    moves = []
    if (c[0] + 1) in range and (c[1] + 2) in range:
        moves.append((alpha[c[0] + 1], c[1] + 2))
    if (c[0] - 1) in range and (c[1] + 2) in range:
        moves.append((alpha[c[0] - 1], c[1] + 2))
    
    if (c[0] + 1) in range and (c[1] - 2) in range:
        moves.append((alpha[c[0] + 1], c[1] - 2))
    if (c[0] - 1) in range and (c[1] - 2) in range:
        moves.append((alpha[c[0] - 1], c[1] - 2))
        
    if (c[0] + 2) in range and (c[1] + 1) in range:
        moves.append((alpha[c[0] + 2], c[1] + 1))
    if (c[0] + 2) in range and (c[1] - 1) in range:
        moves.append((alpha[c[0] + 2], c[1] - 1))
    
    if (c[0] - 2) in range and (c[1] + 1) in range:
        moves.append((alpha[c[0] - 2], c[1] + 1))
    if (c[0] - 2) in range and (c[1] - 1) in range:
        moves.append((alpha[c[0] - 2], c[1] - 1))
    return moves

def createGraph():
    G = {}
    for c0 in alpha:
        for c1 in digits:
            c = (c0, c1)
            for m in getMoves(c):
                make_link(G, c, m)
    return G

def BFS(G, root):
    visited = {}
    deep = {}
    parent = {}
    
    for k in G:
        visited[k] = False
        deep[k] = float('inf')
        parent[k] = None
    
    visited[root] = True
    deep[root] = 0
    
    queue = []
    queue.append(root)
    
    while queue != []:
        n = queue.pop(0)
        for k in G[n]:
            if not visited[k]:
                visited[k] = True
                deep[k] = deep[n] + 1
                parent[k] = n
                queue.append(k)
    return {'visited':visited, 'deep':deep, 'parent':parent}

def solve(G, c1, c2):
    if c1 == c2:
        return 0
    bfs = BFS(G, c1)
    parent = bfs['parent']
    route = []
    while c2 != c1:
        c2 = parent[c2]
        route.append(c2)
    return len(route)


def read():
    G = createGraph()
    lines = sys.stdin.proc().splitlines()
    for line in lines:
        c1, c2 = line.split()
        c1 = (c1[0], int(c1[1]))
        c2 = (c2[0], int(c2[1]))
        print 'To get from', str(c1[0])+str(c1[1]), 'to', str(c2[0])+str(c2[1]), 'takes', solve(G, c1, c2), 'knight moves.'
    return

read()
