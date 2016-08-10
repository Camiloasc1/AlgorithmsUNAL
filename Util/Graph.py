import heapq as Heap

def makeNDLink(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = True
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = True

def makeNDLinkW(G, n1, n2, W, add = False):

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

    if add:
        if n1 not in G[n2]:
            G[n2][n1] = 0
        G[n2][n1] += W
    else:
        G[n2][n1] = W

    return G

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

def BFS(G, root):
    Res = 0
    P = 1

    dist = {}

    for n in G:
        dist[n] = (float('inf'), None)

    dist[root] = (0, root)

    queue = []
    queue.append(root)

    while queue != []:
        n = queue.pop(0)
        for m in G[n]:
            if dist[m][P] == None:
                dist[m] = (dist[n][Res] + 1, n)
                queue.append(m)

    dist[root] = (0, None)
    return dist

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

def BFSClasic(G, root):
    visited = {}
    dist = {}
    parent = {}

    for k in G:
        visited[k] = False
        dist[k] = float('inf')
        parent[k] = None

    visited[root] = True
    dist[root] = 0

    queue = []
    queue.append(root)

    while queue != []:
        n = queue.pop(0)
        for k in G[n]:
            if not visited[k]:
                visited[k] = True
                dist[k] = dist[n] + 1
                parent[k] = n
                queue.append(k)
    return dist, parent, visited

def FloydWarshall(G):
    Res = 0
    P = 1

    dist = {}
    for i in G:
        dist[i] = {}
        for j in G:
            dist[i][j] = (float('inf'), None)
        dist[i][i] = (0, None)
        for neighbor in G[i]:
            dist[i][neighbor] = (G[i][neighbor], i)

    for k in G:
        for i in G:
            for j in G:
                nd = dist[i][k][Res] + dist[k][j][Res]
                if nd < dist[i][j][Res]:
                    dist[i][j] = (nd, dist[k][j][P])

    return dist

def FloydWarshall2(G):
    dist = {}
    parent = {}

    for i in G:
        dist[i] = {}
        parent[i] = {}
        for j in G:
            dist[i][j] = float('inf')
            parent[i][j] = None
        dist[i][i] = 0
        for neighbor in G[i]:
            dist[i][neighbor] = G[i][neighbor]
            parent[i][neighbor] = i

    for k in G:
        for i in G:
            for j in G:
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
                    parent[i][j] = parent[k][j]

    return dist, parent

def Dijkstra(G, root):
    Res = 0
    # P = 1

    dist = {}
    for n in G:
        dist[n] = (float('inf'), None)
    dist[root] = (0, None)

    h = []
    Heap.heappush(h, (0, root))
    while h != []:
        d, n = Heap.heappop(h)
        for m in G[n]:
            nd = d + G[n][m]
            if nd < dist[m][Res]:
                dist[m] = (nd, n)
                Heap.heappush(h, (nd, m))
    return dist

def Dijkstra2(G, root):
    dist = {}
    parent = {}

    for n in G:
        dist[n] = float('inf')
        parent[n] = None
    dist[root] = 0

    h = []
    Heap.heappush(h, (0, root))
    while h != []:
        d, n = Heap.heappop(h)
        for m in G[n]:
            nd = d + G[n][m]
            if nd < dist[m]:
                dist[m] = nd
                parent[m] = n
                Heap.heappush(h, (nd, m))
    return dist, parent

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

def ParentRoute(parent, n1, n2):
    if n1 not in parent or n2 not in parent:
        return None
    if n1 == n2:
        return []
    route = [n2]
    while n1 != n2:
        n2 = parent[n2]
        if n2 == None: # Not connected
            return None
        route.insert(0, n2)
    return route

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
