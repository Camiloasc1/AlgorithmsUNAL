
def Dn(n, A = None, Res = None):
    if A == None or A == {}:
        A = {}
        A[0] = 0
        A[1] = 1
        A[2] = 0
    if Res == None or Res == {}:
        Res = {}
        Res[0] = 0
        Res[1] = 0
        Res[2] = 3
    for i in xrange(max(Res.keys()) + 1, n + 1):
        A[i] = Res[i - 1] + A[i - 2]
        Res[i] = Res[i - 2] + 2 * A[i - 1]
    return A, Res

A, Res = Dn(10)
print A
print Res
A, Res = Dn(100, A, Res)
# print A[10], A[50], A[100]
print Res[10], Res[50], Res[100]
