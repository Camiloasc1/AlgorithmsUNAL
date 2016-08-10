import  sys

def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    # G[n2][n1] = w
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

def read():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n, m, l = map(int, sys.stdin.readline().split())
        # G = dict.fromkeys(xrange(1, n + 1))
        G = {}
        for _ in xrange(m):
            a, b = map(int, sys.stdin.readline().split())
            make_link(G, a, b, True)

        push = []
        for _ in xrange(l):
            v = BFS(G, int(sys.stdin.readline()))['visited']
            push.extend(filter(lambda x: v[x], v))

        print len(list(set(push)))

read()
