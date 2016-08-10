import sys

intervals = []

    
def check(i1, i2):
    if i2[0] < i1[0] < i2[1]:
        return True
    elif i2[0] < i1[1] < i2[1]:
        return True
    else:
        return False

def solve(a, b):
    i1 = intervals[a]
    i2 = intervals[b]
    if check(i1, i2):
        return True
    check = []
    check.append(i1)
    while check != []:
        j1 = check.pop()
        for n1, j2 in enumerate(intervals):
            if n1 == a:
                continue
            if check(j1, j2):
                if j2 == i2:
                    return True
                check.append(j2)
    return False

lc = 0
data = sys.stdin.read().splitlines()
while lc < len(data):
    n = int(data[lc])
    intervals = []
    for i in xrange(n):
        t, a, b = map(int, data[lc + i + 1].split())
        if t == 1:
            intervals.append((a, b))
        elif t == 2:
            if solve(a - 1, b - 1):
                print 'YES'
            else:
                print 'NO'
    lc += n + 1
    
