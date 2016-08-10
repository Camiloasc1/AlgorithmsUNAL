#
# This is the same problem as "Distance Oracle I" except that instead of
# only having to deal with binary trees, the assignment asks you to
# create labels for all tree graphs.
#
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
#
# Given a graph G that is a tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

import math
import heapq as Heap

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

def CloneGraph(G):
    G2 = {}
    for k in G:
        G2[k] = G[k]
    return G2

def mark_component(G, node, marked):
    marked[node] = True
    for neighbor in G[node]:
        if neighbor not in marked:
            mark_component(G, neighbor, marked)
    return marked

#
# create_labels takes in a tree and returns a dictionary, mapping each
# node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#
def create_labels(treeG):
    labels = {}
    # your code here
    # make a copy of treeG
    G2 = CloneGraph(treeG)
    for v in G2.keys():
        labels[v] = {v: 0}
    subtreeG = [G2]
    while subtreeG:
        G = subtreeG.pop()

#         dist, _ = FloydWarshall2(G)
        dist = {}
        for v in G.keys():
            dist[v], _ = Dijkstra2(G, v)

        std_min = float('inf')
        for v in dist.keys():
            sum_ln = 0
            sum_qd = 0
            for w in dist[v].keys():
                sum_ln += dist[v][w]
                sum_qd += dist[v][w] ** 2
            mean = float(sum_ln / len(dist[v]))
            std = float(math.sqrt((sum_qd - mean ** 2) / len(dist[v])))
            if std < std_min:
                std_min = std
                hub = v

        for v in G.keys():
            labels[v][hub] = dist[v][hub]
        for v in G.keys():
            if hub in G[v].keys():
                del G[v][hub]
        del G[hub]
        checked = {}
        for v in G.keys():
            if v not in checked:
                marked = mark_component(G, v, {})
                subG = {}
                for v in marked:
                    subG[v] = G[v]
                    checked[v] = True
                subtreeG.append(subG)
    return labels

#######
# Testing
#


def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances

def make_link(G, node1, node2, weight = 1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree)
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2

test()
