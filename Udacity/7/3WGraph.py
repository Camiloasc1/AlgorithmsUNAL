#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the W was the
# number of C books in which they both appeared.
#
# In this assignment, determine the weights between
# C book characters by giving the probability
# that a randomly chosen C book containing one of
# the characters will also contain the other
#

# from marvel import marvel, characters

def create_weighted_graph(bipartiteG, characters):
    G = {}
    for H1 in characters:
        for C in bipartiteG[H1]:
            for H2 in bipartiteG[C]:
                if H1 != H2 and (H1 not in G or H2 not in G or H1 not in G[H2] or H2 not in G[H1]):
                    H1_C, H2_C = set(bipartiteG[H1].keys()), set(bipartiteG[H2].keys())
                    W = float(len(H1_C & H2_C)) / float(len(H1_C | H2_C))
                    makeNDLinkW(G, H1, H2, W)
    return G

def makeNDLinkW(G, n1, n2, W, add = False):

    if n1 not in G:
        G[n1] = {}

    if add:
        if n2 not in G[n1]:
            G[n1][n2] = 0
        G[n1][n2] += W
    else:
        G[n1][n2] = W

    if n2 not in G:
        G[n2] = {}

    if add:
        if n1 not in G[n2]:
            G[n2][n1] = 0
        G[n2][n1] += W
    else:
        G[n2][n1] = W

    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

# def test2():
#     G = create_weighted_graph(marvel, characters)

test()
