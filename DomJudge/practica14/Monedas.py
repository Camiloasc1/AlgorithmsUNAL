import sys

coins = [1, 5, 10, 25, 50]


def Calc(Res, i):
    if i in Res:
        return Res

    if i in coins:
        Res[i] = 1
    else:
        Res[i] = 0
#     for c in coins[::-1]:
#     for c in coins:
    for c in xrange(i / 2):
        if i - c > 0:
            Res[i] += Calc(Res, c)[c] * Calc(Res, i - c)[i - c]
    return Res

def read():
    Res = {}
    Res[0] = 1
    for c in xrange(20):
        Res[c] = Calc(Res, c)[c]
        print 'Res', c, Res[c]
#     for c in coins:
#         Res[c] = Calc(Res, c)[c]
#         print 'Res', c, Res[c]
    Q = []
    for l in sys.stdin.read().splitlines():
        i = int(l)
        Res = Calc(Res, i)
        print Res[i]

read()
