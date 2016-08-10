import sys

def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    # G[n2][n1] = w
    return G
def make_link2(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = w
    return G

def create_rooted_spanning_tree(G, root):
    S = {}

    visited = {}
    parent = {}

    for k in G:
        visited[k] = False
        parent[k] = None
        S[k] = {}

    visited[root] = True

    queue = []
    queue.append(root)

    while queue != []:
        n = queue.pop(0)
        for k in G[n]:
            make_link(S, n, k, 'red')
            if not visited[k]:
                visited[k] = True
                parent[k] = n
                queue.append(k)

    for k in parent:
        if k != root:
            make_link(S, parent[k], k, 'green')

    return S, visited
def BFS(G, root):
    visited = {}
    deep = {}
    parent = {}
    tree = True

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
            else:
                tree = False
    return {'visited':visited, 'deep':deep, 'parent':parent, 'tree':tree}

def solve(G):
    conected = {}
    for root in G:
        bfs = BFS(G, root)
        if bfs['tree'] == False:
            return False
        visited = bfs['visited']
        conected = True
        for k in G:
            if visited[k] == False:
                conected = False
        if conected == False:
            continue
        return True

    return False

def solve2(G):
    nc = 0
    for root in G:
        S, visited = create_rooted_spanning_tree(G, root)
        # print root, S

        for k in S:
            if visited[k] == False:
                nc += 1
                break
            for l in S[k]:
                if S[k][l] == 'red':
                    return False
    return nc < len(G)

def solve3(G):
    for root in G:
        S, visited = create_rooted_spanning_tree(G, root)
        # print root, S

        for k in S:
            for l in S[k]:
                if S[k][l] == 'red':
                    return False
    return True

def notConected(G):
    root = G.keys()[0]
    push = G.keys()
    for root in G:
        v = BFS(G, root)['visited']
        push = filter(lambda x: not v[x], v)

    return len(list(set(push))) == len(G)

def notConected2(G):
    root = G.keys()[0]
    v = BFS(G, root)['visited']
    push = filter(lambda x: not v[x], v)
    return len(list(set(push))) != 0

def solve4(G):
    dest = []
    nodes = G.keys()
    for k in G:
        for l in G[k]:
            if G[k][l] not in dest:
                dest.append(G[k][l])
    nd = []
    for n in nodes:
        if n not in dest:
            nd.append(n)
    if len(nd) == 0:
        return False
    for root in nd:
        pass
    return False
def solve5(G):
    isTree = True
    for root in G:
        S = {}

        visited = {}
        parent = {}

        for k in G:
            visited[k] = False
            parent[k] = None
            S[k] = {}

        visited[root] = True

        queue = []
        queue.append(root)

        while queue != []:
            n = queue.pop(0)
            for k in G[n]:
                make_link(S, n, k, 'red')
                if not visited[k]:
                    visited[k] = True
                    parent[k] = n
                    queue.append(k)
                else:
                    isTree = False

        for k in parent:
            if k != root:
                make_link(S, parent[k], k, 'green')

        for k in S:
            for l in S[k]:
                if S[k][l] == 'red':
                    isTree = False
        if isTree:
            return True
    return False
# Lectua del codigo
def juez():
    arch = sys.stdin.readlines()
    for line in arch:
        nodes = map(int, line.strip().split())
        G = {}
        myG = {}
        for i in xrange(0, len(nodes), 2):
            if nodes[i] == 0:
                break
            make_link(G, nodes[i], nodes[i + 1], True)
            make_link2(myG, nodes[i], nodes[i + 1], True)

        if G == {}:
            print "it is not a tree."
            continue
        if len(G) == 1:
            print "it is a tree."
            continue
        if notConected2(myG):
            print "it is not a tree."
            continue
        if solve5(G):
            print "it is a tree."
        else:
            print "it is not a tree."
juez()
