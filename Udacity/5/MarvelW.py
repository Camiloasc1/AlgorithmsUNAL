import csv
import Util.Graph as Graph

def test():
    a, b, c, d, e, f, g = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
    triples = (a, c, 3), (c, b, 10), (a, b, 15), (d, b, 9), (a, d, 3), (d, f, 7), (d, e, 3), (e, g, 1), (e, f, 5), (f, g, 2), (b, f, 1)
    G = {}
    for i, j, k in triples:
        Graph.makeNDLinkW(G, i, j, k)

    _, dist = Graph.FloydWarshall2(G)
    _, distA = Graph.Dijkstra2(G, 'A')
    print dist['A']
    print distA
    print dist['A'] == distA
    print
    print Graph.BFSRoute(G, 'A', 'G')
    print Graph.DijkstraRoute(G, 'A', 'G')
    print Graph.ParentRoute(dist['A'], 'A', 'G')
    print Graph.ParentRoute(distA, 'A', 'G')
    print
    print Graph.BFSClasic(G, 'A')
    print Graph.BFS2(G, 'A')
    print Graph.BFS(G, 'A')


def test2(G):
    L = len(G)
    print 'len(G)=', L
    count = 0

    n1 = 'SPIDER-MAN/PETER PAR'
    n2 = 'YAP'

    dj = Graph.Dijkstra2(G, n1)
    bfs = Graph.BFSClasic(G, n1)

    djR = Graph.ParentRouteLen(dj[1], n1, n2)
    bfsD = bfs[0][n2]

    print djR, bfsD
    if djR != bfsD:
        count += 1

    n1 = 'WOLVERINE/LOGAN '
    n2 = 'HOARFROST/'

    dj = Graph.Dijkstra2(G, n1)
    bfs = Graph.BFSClasic(G, n1)

    djR = Graph.ParentRouteLen(dj[1], n1, n2)
    bfsD = bfs[0][n2]

    print djR, bfsD
    if djR != bfsD:
        count += 1

    assert count == 2


def main():
    # Bipartite Util
    tsv = csv.reader(open('marvel.db'), delimiter = '\t')
    G = {}
    p2 = {}
    for n1, n2 in tsv:
        if n2 not in p2:
            p2[n2] = []
        for n in p2[n2]:
            Graph.makeNDLinkW(G, n1, n, 1, add = True)
        p2[n2].append(n1)
    del p2

    for n1 in G:
        for n2 in G[n1]:
            if G[n1][n2] > 1:
                G[n1][n2] = 1.0 / float(G[n1][n2])

    # test2(G)

    count = 0
    '''
    for c, n1 in enumerate(G.keys()):
        dj = Graph.Dijkstra2(G, n1)
        bfs = Graph.BFS2(G, n1)
        for n2 in G:
            if n1 == n2:
                continue
            djR = Graph.ParentRoute(dj[1], n1, n2)
            bfsD = Graph.ParentRoute(bfs[1], n1, n2)
            if djR == None or bfsD == None:
                continue
            if len(djR) != len(bfsD):
                count += 1
        print c, '/', L, ':', count / 2
    '''
    ls = ['SPIDER-MAN/PETER PAR', 'GREEN GOBLIN/NORMAN ', 'WOLVERINE/LOGAN ', 'PROFESSOR X/CHARLES ', 'CAPTAIN AMERICA']
    for n1 in ls:
        dj = Graph.Dijkstra2(G, n1)
        bfs = Graph.BFSClasic(G, n1)
        for n2 in G:
            if n1 == n2:
                continue
            if bfs[2][n2] == False:
                continue
            djR = Graph.ParentRouteLen(dj[1], n1, n2)
            bfsD = bfs[0][n2]
            if djR != bfsD:
                count += 1
    print count

main()
# test()
