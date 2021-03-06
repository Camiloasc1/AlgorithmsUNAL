#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
#
from heapq import *

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

def dijkstra(G, v):
    dist = {}
    parent = {}
    for n in G:
        dist[n] = float('inf')
        parent[n] = None
    dist[v] = 0

    h = []
    heappush(h, (dist[v], v))
    while h != []:
        _, n = heappop(h)
        for m in G[n]:
            if dist[m] > dist[n] + G[n][m]:
                dist[m] = dist[n] + G[n][m]
                parent[m] = n
                heappush(h, (dist[m], m))
    return dist

############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a, b, c, d, e, f, g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a, c, 3), (c, b, 10), (a, b, 15), (d, b, 9), (a, d, 4), (d, f, 7), (d, e, 3),
               (e, g, 1), (e, f, 5), (f, g, 2), (b, f, 1))
    G = {}
    for (i, j, k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 # (a -> d -> e -> g)
    assert dist[b] == 11 # (a -> d -> e -> g -> f -> b)

test()
