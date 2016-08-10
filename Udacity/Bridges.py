# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`
import math

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
def create_rooted_spanning_tree(G, root):
    S = {}
    
    visited = {}
    parent = {}
    
    for k in G:
        visited[k] = False
        parent[k] = None
    
    visited[root] = True
    
    queue = []
    queue.append(root)
    
    while queue != []:
        n = queue.pop(0)
        for k in G[n]:
            make_link(S, n, k, 'red')
            if not visited[k]:
                visited[k] = True
                parent[k] = n
                queue.append(k)
    
    for k in parent:
        if k != root:
            make_link(S, parent[k], k, 'green')
    
    return S

def make_link(G, n1, n2, w):
    if n1 not in G:
        G[n1] = {}
    G[n1][n2] = w
    if n2 not in G:
        G[n2] = {}
    G[n2][n1] = w
    return G

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }
test_create_rooted_spanning_tree()
###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    postOrder = [root]
    
    queue = []
    queue.append(root)
    
    while queue != []:
        n = queue.pop(0)
        # for k in S[n]:
        for k in sorted(S[n]):
            if k not in postOrder and S[n][k] == 'green':
                postOrder.insert(postOrder.index(n), k)
                queue.append(k)
    
    return {n:(i + 1) for i, n in enumerate(postOrder)}

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
test_post_order()
##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    descendants = descendantsList(S, root)
    return {k:len(descendants[k]) for k in descendants}

def BFS(G, root):
    visited = {}
    deep = {}
    parent = {}
    
    for k in G:
        visited[k] = False
        deep[k] = float('inf')
        parent[k] = None
    
    visited[root] = True
    deep[root] = 0
    
    queue = []
    queue.append(root)
    
    while queue != []:
        n = queue.pop(0)
        for k in G[n]:
            if not visited[k]:
                visited[k] = True
                deep[k] = deep[n] + 1
                parent[k] = n
                queue.append(k)
    return {'visited':visited, 'deep':deep, 'parent':parent}

def descendantsList(G, root):
    bfs = BFS(G, root)
    parent = bfs['parent']
    # deep = bfs['deep']
    
    descendants = {}
    for k in G:
        descendants[k] = [k]
    
    for k in parent:
        n = k
        # for _ in xrange(deep[n]):
        while parent[n] != None:
            n = parent[n]
            descendants[n].append(k)
    
    return {k:sorted(descendants[k]) for k in descendants}

def test_number_of_descendants():
    S = {'a': {'c': 'green', 'b': 'green'},
          'b': {'a': 'green', 'd': 'red'},
          'c': {'a': 'green', 'd': 'green'},
          'd': {'c': 'green', 'b': 'red', 'e': 'green'},
          'e': {'d': 'green', 'g': 'green', 'f': 'green'},
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
test_number_of_descendants()
###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    # follow one red edge
    lpo = dict(po)
    for k in S:
        for l in S[k]:
            if S[k][l] == 'red':
                lpo[k] = min([lpo[k], lpo[l]])
    # follow only green edges
    descendants = descendantsList(S, root)
    for k in descendants:
        lpo[k] = min([lpo[l] for l in descendants[k]])
    return lpo

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}

test_lowest_post_order()
################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    # follow one red edge
    hpo = dict(po)
    for k in S:
        for l in S[k]:
            if S[k][l] == 'red':
                hpo[k] = max([hpo[k], hpo[l]])
    # follow only green edges
    descendants = descendantsList(S, root)
    for k in descendants:
        hpo[k] = max([hpo[l] for l in descendants[k]])
    return hpo

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
test_highest_post_order()
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    bridges = []
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)
    
    bfs = BFS(S, root)
    parent = bfs['parent']
    for k in G:
        if k == root:
            continue
        if po[k] >= hpo[k] and lpo[k] > (po[k] - nd[k]):
            bridges.append((parent[k], k))
    
    return bridges

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]
test_bridge_edges()
