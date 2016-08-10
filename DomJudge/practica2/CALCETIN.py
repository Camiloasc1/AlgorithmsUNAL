import sys

data = sys.stdin.read().splitlines()
for line in data:
    n, m = map(int, line.split())
    days = 0
    while n > 0:
        days += 1
        n -= 1
        if days % m == 0:
            n += 1
    print days
