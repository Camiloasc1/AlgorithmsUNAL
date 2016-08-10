import  sys

def move(c1, c2):
    d1, d2 = c1[1] - c1[0], c2[1] - c2[0]
    if d2 >= c1[0]: # c1 emplty
        c1[0], c2[0] = 0, c2[0] + c1[0]
    if d2 < c1[0]: # c2 full
        c1[0], c2[0] = c1[0] - d2, c2[1]
    return [c1, c2]

def solve(ca, cb, cc):
    check = []

    moves = []
    m = [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b']]
    m1 = [[]]
    for _ in xrange(6):
        m2 = m1
        m1 = []
        for i in m:
            for j in m2:
                m1.append([i] + j)
        moves.extend(m1)
    moves = filter(lambda move:move[0][0] == 'c', moves)

    for mov in moves:
        a, b, c = [0, ca], [0, cb], [cc, cc]
        cubetas = {'a':a, 'b':b, 'c':c}
        for m in mov:
            cubetas[m[0]], cubetas[m[1]] = move(cubetas[m[0]], cubetas[m[1]])
        if cubetas['a'][0] == 0:
            if cubetas['c'][0] not in check:
                check.append(cubetas['c'][0])

    return list(set(check))

def solve2(ca, cb, cc):
    moves = []
    m = ['a', 'b', 'c']
    m1 = [['c']]
    for _ in xrange((3 * 2) - 1):
        m2 = m1
        m1 = []
        for k in m2:
            for i in filter(lambda move:k[-1] != move, m):
                    m1.append(k + [i])
        moves.extend(m1)
    print moves
    for m in moves:
        a, b, c = [0, ca], [0, cb], [cc, cc]
        cubetas = {'a':a, 'b':b, 'c':c}
        for i in xrange(len(m) - 1):
            cubetas[m[i]], cubetas[m[i + 1]] = move(cubetas[m[i]], cubetas[m[i + 1]])
        if cubetas['a'][0] == 0:
            print cubetas['c'][0]
    check = []
    # check.extend(moves)
    check.append(cc)
    print move(c, a)
    print move(c, b)
    return check

def read():
    lines = sys.stdin.read().splitlines()
    for l in lines:
        ca, cb, cc = map(int, l.split())
        check = sorted(solve(ca, cb, cc))
        for i in check:
            print i,
        print
read()
