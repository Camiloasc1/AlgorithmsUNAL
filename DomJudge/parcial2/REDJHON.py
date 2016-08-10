import sys

def Dn(n, Res = None):
    if Res == None or Res == {}:
        Res = {}
        Res[0] = 1
        Res[1] = 1
        Res[2] = 1
        Res[3] = 1
        Res[4] = 2
    for i in xrange(max(Res.keys()) + 1, n + 1):
        Res[i] = Res[i - 1] + Res[i - 4]
    return Res

def read():
    Res = Dn(100)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        print Res[int(sys.stdin.readline())]

read()
