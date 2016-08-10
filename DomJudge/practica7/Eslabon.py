import operator
import  sys

# Bridge Edges v4

def make_link(G, n1, n2, w):
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

    return S


def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    postOrder = [root]

    queue = []
    queue.append(root)

    while queue != []:
        n = queue.pop(0)
        # for k in S[n]:
        for k in sorted(S[n]):
            if k not in postOrder and S[n][k] == 'green':
                postOrder.insert(postOrder.index(n), k)
                queue.append(k)

    return {n:(i + 1) for i, n in enumerate(postOrder)}


def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    descendants = descendantsList(S, root)
    return {k:len(descendants[k]) for k in descendants}

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

def descendantsList(G, root):
    bfs = BFS(G, root)
    parent = bfs['parent']
    # deep = bfs['deep']

    descendants = {}
    for k in G:
        descendants[k] = [k]

    for k in parent:
        n = k
        # for _ in xrange(deep[n]):
        while parent[n] != None:
            n = parent[n]
            descendants[n].append(k)

    return {k:sorted(descendants[k]) for k in descendants}

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    # follow one red edge
    lpo = dict(po)
    for k in S:
        for l in S[k]:
            if S[k][l] == 'red':
                lpo[k] = min([lpo[k], lpo[l]])
    # follow only green edges
    descendants = descendantsList(S, root)
    for k in descendants:
        lpo[k] = min([lpo[l] for l in descendants[k]])
    return lpo

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    # follow one red edge
    hpo = dict(po)
    for k in S:
        for l in S[k]:
            if S[k][l] == 'red':
                hpo[k] = max([hpo[k], hpo[l]])
    # follow only green edges
    descendants = descendantsList(S, root)
    for k in descendants:
        hpo[k] = max([hpo[l] for l in descendants[k]])
    return hpo

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    bridges = []
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)

    bfs = BFS(S, root)
    parent = bfs['parent']
    for k in G:
        if k == root:
            continue
        if po[k] >= hpo[k] and lpo[k] > (po[k] - nd[k]):
            bridges.append((parent[k], k))

    return bridges

# Problem

def read():
    n, m = map(int, sys.stdin.readline().split())
    while n != 0 and m != 0:
        G = {}
        for _ in xrange(m):
            a, b = map(int, sys.stdin.readline().split())
            make_link(G, a, b, 1)
        bridges = bridge_edges(G, G.keys()[0])
        bridges.sort(key = operator.itemgetter(0, 1))
        check = str(len(bridges))
        for i in bridges:
            check += ' ' + str(i[0]) + ' ' + str(i[1])
        print check
        n, m = map(int, sys.stdin.readline().split())

read()
