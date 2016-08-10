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

def count(G, e):
    if e not in G:
        return 0
    mats = []
    for k in G[e]:
        for m in G[e][k]:
            if m not in mats:
                mats.append(m)
    return len(mats)

def solve(G, m):
    # solucion ACA
    est = []
    for k in G:
        for l in G[k]:
            if m in G[k][l]:
                if k not in est:
                    est.append(k)
                if l not in est:
                    est.append(l)
    mats = []
    for e in est:
        mats.append(count(G, e))
    if len(mats) == 0:
        return 0
    return sum(mats) / len(mats)

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
        m = data[0]
        print solve(G , m)
        k += 1
    
    case += 1
