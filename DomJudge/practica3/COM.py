import sys

def misterio1(n):
    count = 4  #
    s = 0
    i = 1
    while (i < n):
        count += 4  #
        j = i + 1
        while (j <= n):
            count += 4  #
            k = 1
            while (k <= j):
                count += 3  #
                s += 2
                k += 1
            j += 1
        i += 1
    # return s
    return count

def misterio2(n):
    count = 4  #
    x = 1
    i = 0
    while i < n:
        count += 3  #
        i += 1
        x = x * 2
    # return x
    return count

lines = sys.stdin.read().splitlines()

for line in lines:
    f, n = map(int, line.split())
    if f != 0:
        if f == 1:
            print misterio1(n)
        elif f == 2:
            print misterio2(n)
        else:
            print 0

