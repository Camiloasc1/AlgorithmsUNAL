import sys

# modificar esta funcion
def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    if n2 not in G[n1]:
        G[n1][n2] = []
    G[n1][n2].append(w)
    if n2 not in G:
        G[n2] = {}
    if n1 not in G[n2]:
        G[n2][n1] = []
    G[n2][n1].append(w)
    return G


def solve(G, u, v):
    # solucion ACA
    if u not in G or v not in G:
        return None
    check = []
    for k in G[u]:
        if k == v:
            for j in G[u][v]:
                if j not in check:
                    check.append(j)
    return sorted(check)

TC = int(sys.stdin.readline())
case = 0
while case < TC:
    G = {}
    line = sys.stdin.readline().strip()
    line = line.split()
    nNodes = int(line[0])
    nQ = int(line[1])
    k = 0
    while(k < nNodes):
        line = sys.stdin.readline().strip()
        data = line.split()
        u = data[0]
        v = data[1]
        m = data[2] 
        make_link(G, u, v, m)
        k += 1
    # print "Gafo::", G
    k = 0
    
    print "Case %d:" % (case + 1)
    while(k < nQ):
        line = sys.stdin.readline().strip()
        data = line.split()
        u = data[0]
        v = data[1]
        sol = solve(G , u , v)
        if sol == None or len(sol) == 0:
            print "*"
        else:
            check = ""
            for s in sol:
                check += s + ", "
            print check[:-2]
        k += 1
    
    case += 1
