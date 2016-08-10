import Util.Graph as Graph

G = {}
G[1] = {1:0, 2:2, 3:11, 4:12}
G[2] = {2:0, 3:3, 4:6}
G[3] = {3:0, 4:1}
G[4] = {1:2, 4:0}

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
        print dist, parent
    return dist, parent

FloydWarshall2(G)

dist, parent = Graph.Dijkstra2(G, 2)
print dist, parent
