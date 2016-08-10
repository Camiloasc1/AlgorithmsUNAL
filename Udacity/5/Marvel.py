import csv
import random

def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = w
    return G

def split(L):
    p = random.choice(L)
    l, r = [], []
    m = 0
    for e in L:
        if e < p:
            l.append(e)
        elif e > p:
            r.append(e)
        else:
            m += 1

    return l, [p] * m, r

def quickSort(L):
    if len(L) <= 1:
        return L
    l, m, r = split(L)
    return quickSort(l) + m + quickSort(r)

def quickSearch(L, pos):
    if len(L) <= 1:
        return L
    l, m, r = split(L)
    if len(l) > pos: # In l
        return quickSearch(l, pos)
    elif len(l) + len(m) > pos: # In m
        return m[0]
    else: # In r
        return quickSearch(r, pos - (len(l) + len(m)))

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter = '\t')
    G = {}
    n1, n2 = [], []
    for (node1, node2) in tsv:
        make_link(G, node1, node2, 1)
        if node1 not in n1:
            n1.append(node1)
        if node2 not in n2:
            n2.append(node2)
    return G, n1, n2

def main():
    # Read the marvel comics graph
    G1, heroes, comics = read_graph('marvel.db')
    G2 = {}

    for h1 in heroes:
        for h2 in heroes:
            make_link(G2, h1, h2, 0)

    m = (0,)
    for c in comics:
        H = G1[c].keys()
        for h1 in xrange(len(H)):
            for h2 in xrange(h1 + 1, len(H)):
                v = G2[H[h1]][H[h2]] + 1
                G2[H[h1]][H[h2]] = v
                if v > m[0]:
                    m = (v, H[h1], H[h2])
    print m

def makeNDLinkW(G, n1, n2, W):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = W
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = W
    return G

def makeNDLinkWAdd(G, n1, n2, W):
    if n1 not in G:
        G[n1] = {}
    if n2 not in G[n1]:
        G[n1][n2] = 0
    G[n1][n2] += W
    if n2 not in G:
        G[n2] = {}
    if n1 not in G[n2]:
        G[n2][n1] = 0
    G[n2][n1] += W
    return G

def delNDLink(G, n1, n2):
    del G[n1][n2]
    del G[n2][n1]
    return G

def main2():
    # Bipartite Util
    tsv = csv.reader(open('marvel.db'), delimiter = '\t')
    G = {}
    p2 = {}
    for n1, n2 in tsv:
        if n2 not in p2:
            p2[n2] = []
        for n in p2[n2]:
            makeNDLinkWAdd(G, n1, n, 1)
        p2[n2].append(n1)

    m = (0,)
    for n1 in G:
        for n2 in G[n1]:
            if G[n1][n2] > m[0]:
                m = (G[n1][n2], n1, n2)
    print m

main2()
