import sys

def solve2(n, m):
    if n == 1 and m == 1:
        return []
    check = []
    count = 1
    for i in xrange(n):
        for j in xrange(m):
            if j + 1 <= m and (count + 1 <= (n * m)) and not(count + 1 > m * (i + 1)):
                check.append([count, count + 1])
            if (i + 1 <= n) and ((m * (i + 1)) + j + 1 <= (n * m)):
                check.append([count, (m * (i + 1)) + j + 1])
            count += 1
    return check

def solve(n1, m):
    if n1 == 1 and m == 1:
        return []
    
    G = []
    count = 1
    for i in xrange(n1):
        G.append([])
        for j in xrange(m):
            G[i].append(count)
            count += 1
    check = []
    for i in xrange(n1):
        for j in xrange(m):
            if j + 1 < m:
                check.append([G[i][j], G[i][j + 1]])
            if i + 1 < n1:
                check.append([G[i][j], G[i + 1][j]])
            count += 1
    return check

def printList(edges): 
    i = 0 
    check = "" 
    for edge in edges: 
        if i < 1: 
            i = 1 
            check += str(edge[0]) + "-" + str(edge[1]) 
        else: 
            check += " " + edge[0].__str__() + "-" + edge[1].__str__() 
    print check

def gridGraph(): 
    input = sys.stdin.read().splitlines()
    for line in input: 
        nums = line.split() 
        n = int(nums[0]) 
        m = int(nums[1]) 
        edgeList = solve(n, m) 
        printList(edgeList) 
 
gridGraph()
