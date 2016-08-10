import sys

def make_link(G, n1, n2):
    if n1 not in G:
        G[n1] = {}
    (G[n1])[n2] = 1
    if n2 not in G:
        G[n2] = {}
    (G[n2])[n1] = 1
    return G

# funcion que retorna una lista de tres numeros con el numero de vertices

# que tienen una distacia minima de 1, 2 y 3 respectivamente a un vertice dado

def count_vertices(G, node):
    sol = [0, 0, 0]
    if node not in G:
        return sol
    # 1
    nodes1 = []
    for k in G[node]:
        if k != node and k not in nodes1:
            nodes1.append(k)
    sol[0] = len(nodes1)
    # 2
    nodes2 = []
    for k in G[node]:
        for l in G[k]:
            if l != node and (l not in nodes1) and (l not in nodes2):
                nodes2.append(l)
    sol[1] = len(nodes2)
    # 3
    nodes3 = []
    for k in G[node]:
        for l in G[k]:
            for m in G[l]:
                if m != node and (m not in nodes1) and (m not in nodes2) and (m not in nodes3):
                    nodes3.append(m)
    sol[2] = len(nodes3)
    return sol

def test():
    tests = [[(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)], [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 7), (5, 7), (6, 7)]]
    sol = [[2, 2, 1], [2, 4, 1]]
    for i in range(2):
        G = {}
        for edge in tests[i]:
            make_link(G, edge[0], edge[1])
        current_sol = count_vertices(G, 0)
        if cmp(current_sol, sol[i]) == 0:
            print "case " + str(i + 1) + ": correct"
        else:
            print "case " + str(i + 1) + ": wrong answer"

# test()

TC = int(sys.stdin.readline())

while TC:
    G = {}
    line = sys.stdin.readline().strip() 
    nodes_edges = line.split()
    n = int(nodes_edges[0])
    e = int(nodes_edges[1])
    while e:
        line = sys.stdin.readline().strip()
        edges = line.split()
        make_link(G, int(edges[0]), int(edges[1]))
        e -= 1
    sol = count_vertices(G, 0)
    for i in sol:
        print i
    TC -= 1
