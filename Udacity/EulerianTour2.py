# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def graphGrades(graph):
    grades = {}
    for i, j in graph:
        if i not in grades:
            grades[i] = 0
        grades[i] += 1
        if j not in grades:
            grades[j] = 0
        grades[j] += 1
    return grades

def find_eulerian_tour(graph):
    start = graph[0][0]
    current = graph[0][1]
    del graph[0]
    
    check = []
    check.append(start)
    
    while len(graph) > 0:
        for i, j in graph:
            if i == current:
                check.append(i)
                current = j
                del graph[graph.index((i, j))]
                break
            if j == current:
                check.append(j)
                current = i
                del graph[graph.index((i, j))]
                break
        else:
            subres = find_eulerian_tour(graph)
            while subres[0] not in check:
                subres.append(subres[1])
                del subres[0]
            pos = check.index(subres[0]) + 1
            for i in subres[1:]:
                check.insert(pos, i)
                pos += 1
    # current == start if all is OK
    if current != start:
        print "Fail"
        return []
    check.append(current)
    return check

#print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
#print find_eulerian_tour([(1, 2), (3, 1), (2, 3)])
# [1, 2, 3, 1]
#print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5),
#                          (3, 6), (8, 9)])
# [0, 1, 7, 3, 6, 1, 5, 4, 8, 9, 5, 2, 4, 0]
print find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10),
                          (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)])
