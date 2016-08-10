import sys

def count(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return count

values = sys.stdin.read().splitlines()
for val in values:
    a, b = map(int, val.split())
    print a, b,
    print max([count(i) for i in xrange(a, b)])
